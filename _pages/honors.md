---
title: ""
layout: single
permalink: /honors/
classes: honors
---

<style>
  /* Hide sidebar only on this page */
  .sidebar { display: none; }
  .page { padding-left: 0 !important; }

  /* Base Spacing System */
  .content-block {
    margin-bottom: 6rem;
  }
  .content-block:last-child {
    margin-bottom: 1rem;
  }

  /* Full width container */
  .full-width-container {
    width: calc(100vw - 100px);
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: calc(-50vw + 50px);
    margin-right: -50vw;
    padding: 0 2rem;
    box-sizing: border-box;
  }

  /* Universal Image Row Styles */
  .image-row {
    display: flex;
    justify-content: center;
    gap: 2rem;
    height: 550px;
  }

  /* Image Column Styles */
  .image-col {
    flex: 1;
    max-width: 100%;
    text-align: center;
    display: flex;
    flex-direction: column;
  }

  /* Image Wrapper */
  .image-wrapper {
    flex: 1;
    display: flex;
    align-items: flex-start;
    justify-content: flex-end;
    overflow: hidden;
  }

  /* Image Styles */
  .image-col img {
    width: 100%;
    height: auto;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    object-fit: contain;
    object-position: bottom;
  }

  /* Caption Styles */
  .image-caption {
    margin-top: 0.5rem;
    font-size: 0.95em;
  }
  .image-caption a {
    color: #0066cc;
    text-decoration: none;
  }

  /* Shared Caption Container */
  .shared-caption {
    flex: 2;
    text-align: center;
    margin-top: 1rem;
  }

  /* Layout Variations */
  .layout-pair-group {
    justify-content: flex-start;
  }
  .pair-group {
    display: flex;
    gap: 0.5rem;
    flex: 1.5;
    position: relative;
  }
  .pair-images {
    display: flex;
    gap: 0.5rem;
    width: 100%;
  }
  .layout-single .image-col {
    max-width: 70%;
    margin: 0 auto;
  }
  .layout-two .image-col {
    max-width: 45%;
  }

  /* Remove forced heights so images and captions flow naturally */
.image-row {
  align-items: flex-start;
  height: auto;
}

.image-wrapper {
  height: auto;
}

/* Consistent spacing between image and caption */
.image-wrapper + .image-caption,
.shared-caption {
  margin-top: 0.4rem; /* unified gap */
}

/* Optional: ensure captions don't stretch the row */
.image-caption, .shared-caption {
  line-height: 1.3;
}

.layout-two .image-col img {
  width: 100%;
  height: 100%;
  object-fit: cover;        /* fills the box; crops overflow */
  display: block;
}

</style>

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