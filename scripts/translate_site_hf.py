import os, pathlib, re, sys
import frontmatter
import torch

# ---------- Settings ----------
SRC_DIRS = ["_pages"]          # add "_posts" if you want posts too
SRC_ROOT_FILES = ["index.md"]  # root-level pages to include if present
EXCLUDE_BASENAMES = {"404.md"}  # skip pages Jekyll expects only at root
DESTS = {
    "de": {"label": "Deutsch", "model": "Helsinki-NLP/opus-mt-en-de"},
    "ru": {"label": "Русский", "model": "Helsinki-NLP/opus-mt-en-ru"},
}
CHUNK_SIZE = 600   # smaller chunks reduce risk of long-seq issues
MAX_IN_LEN = 512   # tokenizer truncation
MAX_OUT_LEN = 1024 # generation cap
NUM_BEAMS = 4      # quality/speed tradeoff
# ------------------------------

# ---- Protection of non-translatable spans ----
TRIPLE_CODE_RE = re.compile(r"```.*?```", re.DOTALL)      # ```code```
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")                  # `code`
MATH_BLOCK_RE  = re.compile(r"\$\$.*?\$\$", re.DOTALL)     # $$math$$
MATH_INLINE_RE = re.compile(r"(?<!\$)\$[^$\n]+\$(?!\$)")   # $math$
HTML_TAG_RE    = re.compile(r"</?[^>]+>")                  # <tags ...>
MD_LINK_RE     = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")    # [text](url)
MD_IMG_RE      = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")   # ![alt](url)
LIQ_TAG_RE     = re.compile(r"{%.*?%}", re.DOTALL)         # {% ... %}
LIQ_VAR_RE     = re.compile(r"{{.*?}}", re.DOTALL)         # {{ ... }}

def protect(text):
    placeholders = {}

    def stash(pattern, key, s):
        idx = 0
        def repl(m):
            nonlocal idx
            token = f"__{key}_{idx}__"
            placeholders[token] = m.group(0)
            idx += 1
            return token
        return pattern.sub(repl, s)

    t = text
    # IMPORTANT: protect Liquid first, then everything else
    for pat, key in [
        (LIQ_TAG_RE,  "LIQTAG"),
        (LIQ_VAR_RE,  "LIQVAR"),
        (TRIPLE_CODE_RE, "TRI"),
        (MATH_BLOCK_RE,  "MB"),
        (MATH_INLINE_RE, "MI"),
        (INLINE_CODE_RE, "INL"),
        (HTML_TAG_RE,    "TAG"),
    ]:
        t = stash(pat, key, t)

    # Then handle links/images (special treatment later)
    link_map = {}
    def link_repl(m):
        token = f"__LINK_{len(link_map)}__"
        link_map[token] = (m.group(1), m.group(2))   # (text, url)
        return token
    t = MD_LINK_RE.sub(link_repl, t)

    img_map = {}
    def img_repl(m):
        token = f"__IMG_{len(img_map)}__"
        img_map[token] = (m.group(1), m.group(2))    # (alt, url)
        return token
    t = MD_IMG_RE.sub(img_repl, t)

    return t, placeholders, link_map, img_map

def split_into_chunks(s: str, maxlen: int):
    parts, buf, cur = [], [], 0
    paras = s.split("\n\n")
    for p in paras:
        if cur + len(p) + 2 <= maxlen:
            buf.append(p); cur += len(p) + 2
        else:
            if buf: parts.append("\n\n".join(buf))
            if len(p) > maxlen:
                for i in range(0, len(p), maxlen):
                    parts.append(p[i:i+maxlen])
                buf, cur = [], 0
            else:
                buf, cur = [p], len(p)
    if buf: parts.append("\n\n".join(buf))
    return parts if parts else [s]

# --- Marian-specific translation (robust on Windows/CPU) ---
from transformers import MarianMTModel, MarianTokenizer

_pipe_cache = {}

def get_marian(lang_code):
    if lang_code in _pipe_cache:
        return _pipe_cache[lang_code]
    model_name = DESTS[lang_code]["model"]
    tok = MarianTokenizer.from_pretrained(model_name, use_fast=False)
    mdl = MarianMTModel.from_pretrained(model_name)
    mdl.eval()
    _pipe_cache[lang_code] = (tok, mdl)
    return tok, mdl

@torch.inference_mode()
def translate_marian(text: str, lang_code: str) -> str:
    tok, mdl = get_marian(lang_code)
    # encode, truncate safely
    enc = tok(
        text,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=MAX_IN_LEN,
    )
    out = mdl.generate(
        **enc,
        max_length=MAX_OUT_LEN,
        num_beams=NUM_BEAMS,
        early_stopping=True,
        no_repeat_ngram_size=3,
    )
    dec = tok.batch_decode(out, skip_special_tokens=True)
    return dec[0]

def translate_body(body: str, lang_code: str):
    # Protect spans that must not change
    protected, placeholders, link_map, img_map = protect(body)

    # Chunk and translate
    chunks = split_into_chunks(protected, CHUNK_SIZE)
    out_chunks = []
    for ck in chunks:
        out_chunks.append(translate_marian(ck, lang_code))
    merged = "\n\n".join(out_chunks)

    # Restore links/images (translate only text/alt)
    def translate_inline(s: str) -> str:
        s2 = s.strip()
        return translate_marian(s2, lang_code) if s2 else s2

    for token, (txt, url) in link_map.items():
        merged = merged.replace(token, f"[{translate_inline(txt)}]({url})")
    for token, (alt, url) in img_map.items():
        t_alt = translate_inline(alt) if alt else ""
        merged = merged.replace(token, f"![{t_alt}]({url})")

    # Restore protected tokens (reverse length to avoid partial overlaps)
    for token in sorted(placeholders.keys(), key=len, reverse=True):
        merged = merged.replace(token, placeholders[token])

    return merged

def target_permalink(meta: dict, lang: str, src_path: pathlib.Path) -> str:
    p = meta.get("permalink")
    if p:
        if not p.startswith("/"): p = "/" + p
        if not p.endswith("/"):  p = p + "/"
        return f"/{lang}{p}"
    return f"/{lang}/{src_path.stem}/"

def translate_page(src_path: pathlib.Path, lang: str):
    post = frontmatter.load(str(src_path))
    meta = dict(post.metadata)
    body = post.content

    # Translate title (short, but may contain markup)
    title = meta.get("title")
    if isinstance(title, str) and title.strip():
        try:
            meta["title"] = translate_body(title, lang)
        except Exception:
            pass  # keep English if anything odd occurs

    meta["lang"] = lang
    meta["permalink"] = target_permalink(meta, lang, src_path)

    tbody = translate_body(body, lang)

    out_dir = pathlib.Path(lang)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / src_path.name
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(frontmatter.dumps(frontmatter.Post(tbody, **meta)))
    print(f"[{lang}] {src_path} -> {out_path}  ({meta['permalink']})")

def collect_sources():
    files = []
    for d in SRC_DIRS:
        p = pathlib.Path(d)
        if p.is_dir():
            files += list(p.rglob("*.md"))
    for f in SRC_ROOT_FILES:
        p = pathlib.Path(f)
        if p.exists():
            files.append(p)
    # avoid re-processing translated trees & excluded basenames
    files = [
        p for p in files
        if p.parts and p.parts[0] not in ("de","ru") and p.name not in EXCLUDE_BASENAMES
    ]
    return sorted(files, key=lambda x: str(x))


def main():
    src = collect_sources()
    if not src:
        print("No source Markdown files found.")
        return
    for lang in DESTS.keys():
        for path in src:
            translate_page(path, lang)

if __name__ == "__main__":
    main()
