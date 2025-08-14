---
title: ""
layout: single
permalink: /honors/
classes: honors
---

<style>
/* ===== Honors page: MOBILE-ONLY layout (desktop untouched) ===== */
@media (max-width: 768px) {
  /* Hide sidebar only on this page (mobile) */
  .honorsmobile .sidebar { display: none; }
  .honorsmobile .page { padding-left: 0 !important; }

  /* Container should be full width on phones */
  .honorsmobile .full-width-container {
    width: 100vw !important;
    left: auto !important;
    right: auto !important;
    margin: 0 !important;
    padding: 0 1rem !important;
    box-sizing: border-box;
  }

  /* Stack rows/cols vertically; kill fixed heights */
  .honorsmobile .image-row {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    gap: 1rem;
    height: auto !important;
  }
  .honorsmobile .paired-images-container,
  .honorsmobile .separate-image,
  .honorsmobile .image-col,
  .honorsmobile .pair-images,
  .honorsmobile .image-wrapper {
    width: 100% !important;
    height: auto !important;
    display: block;
  }

  /* If any pair/group was side-by-side, stack it too */
  .honorsmobile .pair-images { display: flex; flex-direction: column; gap: 0.5rem; }

  /* Images: full-width, no cropping; override inline heights */
  .honorsmobile img,
  .honorsmobile figure img {
    display: block;
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
    object-fit: contain !important;
    object-position: center !important;
    margin: 0 auto 0.75rem;
  }

  /* Captions: slightly smaller, centered */
  .honorsmobile .image-caption,
  .honorsmobile .shared-caption,
  .honorsmobile figcaption {
    font-size: 0.9em;
    line-height: 1.35;
    text-align: center;
    margin-top: 0.4rem !important;
  }

  /* Safety: neutralize any floats */
  .honorsmobile img,
  .honorsmobile figure,
  .honorsmobile .align-left,
  .honorsmobile .align-right {
    float: none !important;
    clear: both !important;
  }

  /* Prevent horizontal scroll from long text */
  .honorsmobile {
    overflow-wrap: anywhere;
    word-break: break-word;
  }
}
</style>

<div class="honorsmobile">
<!-- First Row: 2 Images with Shared Caption + 1 Separate -->
<div class="full-width-container content-block">
  <div class="image-row layout-pair-group">
    <!-- Pair with shared caption -->
    <div class="paired-images-container">
      <div class="pair-images">
        <div class="image-col">
          <div class="image-wrapper">
            <img src="/assets/images/dresden_2.png" alt="Award ceremony 1" style="height: 100%; object-position: bottom;">
          </div>
        </div>
        <div class="image-col">
          <div class="image-wrapper">
            <img src="/assets/images/dresden_3.png" alt="Award ceremony 2" style="height: 100%; object-position: bottom;">
          </div>
        </div>
      </div>
      <div class="shared-caption">
        Award ceremony at TU Dresden for my <a href="https://example.com" target="_blank">Distinguished Research Fellowship</a> (2024).
      </div>
    </div>
    
    <!-- Separate image with its own caption -->
    <div class="image-col separate-image">
      <div class="image-wrapper">
        <img src="/assets/images/dresden_1.png" alt="Teaching session" style="height: 100%;">
      </div>
      <div class="image-caption">
        Teaching chance constrained optimization to PhD students in the <a href="https://example.com" target="_blank">Saxon Doctoral Program</a> (2024).
      </div>
    </div>
  </div>
</div>

<style>
  .layout-pair-group {
    justify-content: flex-start;  
    align-items: stretch; /* Makes all items same height */
    height: 350px; /* Fixed height for entire row */
  }
  
  .paired-images-container {
    flex: 1.5;
    display: flex;
    flex-direction: column;
    height: 100%;
  }
  
  .pair-images {
    display: flex;
    gap: 0.5rem;
    height: calc(100% - 2rem); /* Accounts for caption space */
  }
  
  .image-col {
    height: 100%;
  }
  
  .image-wrapper {
    height: 100%;
  }
  
  .shared-caption {
    text-align: center;
    margin-top: 0.5rem;
    height: 1.5rem;
  }
  
  .separate-image {
    flex: 1;
    display: flex;
    flex-direction: column;
    height: 100%;
  }
</style>

<style>
  /* Unified caption spacing for all rows */
  .image-caption {
    margin-top: 0.5rem; /* Default spacing */
  }

  /* Tighter spacing for specific layouts */
  .layout-two .image-caption,
  .layout-single .image-caption {
    margin-top: 0.2rem; /* Tighter spacing for these layouts */
  }

  /* Adjust spacing based on image height */
.image-wrapper + .image-caption {
  margin-top: 0.5rem;
}
.image-wrapper[style*="height:"] + .image-caption {
  margin-top: 0.2rem;
}
</style>



<!-- Second Row: 2 Images -->
<div class="full-width-container content-block">
  <div class="image-row layout-two">
    <div class="image-col">
      <div class="image-wrapper">
        <img src="/assets/images/erzurum.jpg" alt="Erzurum event" style ="height: 430px; width: 800px;">
      </div>
      <div class="image-caption">
        Honored by the <a href="https://example.com" target="_blank">Ataturk University</a> (2023).
      </div>
    </div>
    <div class="image-col">
      <div class="image-wrapper">
        <img src="/assets/images/humboldt.jpg" alt="Humboldt event" style ="height: 430px; width: auto;">
      </div>
      <div class="image-caption">
        <a href="https://example.com" target="_blank">Short Term Grantee</a> by Humboldt Centre (2024).
      </div>
    </div>
  </div>
</div>

<!-- Third Row: 2 Images -->
<div class="full-width-container content-block">
  <div class="image-row layout-two">
    <div class="image-col">
      <div class="image-wrapper">
        <img src="/assets/images/fefu.png" alt="FEFU TV appearance">
      </div>
      <div class="image-caption">
        In the live-TV show <a href="https://example.com" target="_blank">Live with an Academic</a> explaining integer programming to public in the Far Eastern Federal University Vladivostok with Evgenii A. Nurminskii (2021).
      </div>
    </div>
    <div class="image-col">
      <div class="image-wrapper">
        <img src="/assets/images/ras.png" alt="Russian Academy of Sciences" style ="height: 330px; width: auto;">
      </div>
      <div class="image-caption">
        Invited lecture at Russian Academy of Sciences (2015).
      </div>
    </div>
  </div>
</div>

<!-- Fourth Row: Single Image -->
<div class="full-width-container content-block">
  <div class="image-row layout-single">
    <div class="image-col">
      <div class="image-wrapper">
        <img src="/assets/images/collage.jpg" alt="Collage of talks">
      </div>
      <div class="image-caption">
        Some other talks and awards worldwide.
      </div>
    </div>
  </div>
</div>

</div>