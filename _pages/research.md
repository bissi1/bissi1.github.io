---
title: "Research Portfolio"
permalink: /research/
layout: archive
classes: full
---

My research develops mathematical models and computational algorithms for decision-making under uncertainty. My particular interests are stochastic optimization, chance-constrained programming, fairness-aware methods, and large-scale discrete optimization. 
Two themes shape much of my work:
<div class="square-bullets">
  <ul>
    <li><em>Optimization under uncertainty</em>: how to make high-stakes decisions when future information is imperfect?</li>
    <li><em>Foundations of fairness</em>: how to characterize fairness axiomatically through a model's optimality conditions?</li>
  </ul>
</div>

My research is grounded in mathematical theory but always motivated by real-world challenges. Key application areas include public-health preparedness, infectious disease outbreaks, energy-system planning, sustainability, and resource allocation (details below). Over the past 15 years, I have collaborated with governments, public agencies, and research institutes across the US, Europe, and Asia.

<strong> Selected funding agencies and partners:</strong>
<img src="/assets/images/funding.png" alt="Interdisciplinary Research" style="display:block; max-width:50%; height:auto; margin-bottom:1.5rem;">

## Optimization Under Uncertainty

<div class="research_section_wrapper">
  <div class="research_subsection">
    <div class="research_subsection_text">
      <p>
        Many important decisions must be made before future conditions are known. Examples include planning healthcare systems, designing energy infrastructure, allocating resources, or managing critical risks. My research investigates how optimization models can support such decisions while explicitly accounting for uncertainty.
      </p>
      <p>
      My specific focus is <em>chance-constrained optimization</em>, where decisions must satisfy guaranteed reliability requirements despite uncertain future outcomes. These models provide a mathematically rigorous framework for balancing risk and performance, but are often computationally challenging to solve. My work develops approximations of joint chance constraints to establish theoretical guarantees for such stochastic optimization models. <span class="inline-toggle" onclick="toggleDetails(this)">[Click for more →]</span>      
      </p>
    </div>

    <div class="research_subsection_image">
      <div style="text-align: center; margin-bottom: 0.5em; font-weight: bold;">
        Satisfying a joint chance constraint is an intersection of "successes". <br>
        <a href="https://link.springer.com/article/10.1007/s11590-019-01387-z" style="color: #0066cc; text-decoration: underline;">Explore →</a>
      </div>
      <img src="/assets/images/venn_diagram.png" alt="Probabilistic Bounds" />
    </div>
  </div>

  <div class="inline-details" style="display: none; margin-top: 1em;">
    <p>
      This research originated during my doctoral studies and was significantly advanced through a US Department of Energy grant awarded during my time at Sandia National Laboratories. A central theme has been the development of new bounds for joint chance-constrained optimization models, drawing upon a line of research dating back to Boole, Bonferroni, Fréchet, and related classical results in probability theory.
    </p>

    <p>
    My work establishes connections between classical probability inequalities and practical stochastic optimization. While probability union bounds are traditionally evaluated according to how tightly they approximate the underlying chance constraint, my research demonstrates that stronger theoretical bounds on the constraint do not necessarily yield stronger objective bounds in practice. Or, due to computational limitations, the best approximation of a feasible region may fail to produce the strongest bound on the optimal objective value. The resulting research has contributed to both probability theory and stochastic optimization. Two representative publications include
<a href="https://link.springer.com/article/10.1007/s11590-019-01387-z">this article</a> and
<a href="https://link.springer.com/article/10.1007/s11590-020-01592-1">its follow-up</a>.
</p>

    <p>
     My current work is extending these ideas to broader classes of stochastic optimization models, including ongoing research with my PhD student.
    </p>
  </div>
</div>

## Sustainability & Climate Change

<div class="research_section_wrapper">
  <div class="research_subsection">
    <div class="research_subsection_text">
      <p>
        As several countries advance towards <em>Net-Zero</em> goals (e.g., Germany's <em>Energiewende</em> or France's <em>Transition Énergétique</em>), joint chance constraints have proven especially effective for ensuring highly reliable operation of critical energy systems under uncertain renewable energy availability, such as photovoltaic (PV) systems and coupled wind–diesel systems. Mathematical optimization models for such systems often present significant challenges due to their (a) structure and (b) scale, necessitating the development of heuristics and algorithms.
      </p>
      <p>
        My research has designed modern <em>machine learning</em>-inspired iterative algorithms and employed Lagrangian-based proximal terms to tackle these challenges. See this 
        <a href="https://link.springer.com/article/10.1007/s10287-018-0309-x">older article</a> and this 
        <a href="https://link.springer.com/article/10.1007/s10898-021-01041-y">newer article</a>.
        <span class="inline-toggle" onclick="toggleDetails(this)">[Click for more →]</span>
      </p>
    </div>

    <div class="research_subsection_image">
      <div style="text-align: center; margin-bottom: 0.5em; font-weight: bold;">
        Several European countries are investing in renewable energy sources.
      </div>
      <img src="/assets/images/german_energy.png" alt="Sustainability & Climate Change" />
    </div>
  </div>

  <div class="inline-details" style="display: none; margin-top: 1em;">
    <div class="square-bullets">
      <ul>
        <li>At Sandia National Labs, US (2016–19), I focused on solving large-scale energy system models, addressing critical risks faced by the US electrical grid. Many of these works are available on the <em>US Department of Energy's</em> Office of Scientific and Technical Information website. Access 
          <a href="https://www.osti.gov/search/semantic:bismark%20singh">here →</a>.
        </li>
        <li>At FAU Erlangen–Nürnberg, Germany (2019–22), I led the chair’s research contributions to the multi-institute <code>METIS</code> research collaboration with the <em>Jülich Research Center</em>. This project develops open-source tools for optimizing large-scale energy system models under the framework of Germany's <em>Energiewende</em>.
          <div class="square-bullets">
            <ul>
              <li>Learn more about the METIS project <a href="https://www.fz-juelich.de/en/ice/ice-2/projects/metis?expand=translations,fzjsettings,nearest-institut">here →</a>.</li>
              <li>Explore the technical details of the ETHOS.FINE package <a href="https://github.com/FZJ-IEK3-VSA/FINE" style="color: #0066cc; text-decoration: underline;">here →</a>.</li>
            </ul>
          </div>
        </li>
      </ul>
    </div>
    <p>
      This research not only advances mathematical optimization but also contributes to global sustainability goals, ensuring renewable energy systems remain both efficient and reliable under uncertainty.
    </p>
  </div>
</div>

## Fairness & Waste Management

<div class="research_section_wrapper">
  <div class="research_subsection">
    <div class="research_subsection_text">
     <p>
  In 2020, I began exploring <em>undesirable facility location problems</em> (FLPs) with a unique perspective: ensuring fairness from the point of view of the facilities, rather than the users, which is the typical approach in existing literature. Motivated by applications in waste management, particularly in the context of <em>recycling centers</em> (e.g., UK <em>tips</em> or German <em>Wertstoffhöfe</em>), I lead a diverse team of researchers on this subtopic.
</p>
<p>
  Supported by the <em>Bavarian State Ministry for Science & Arts</em> and the <em>University of Southampton</em>, my team develops discrete optimization models that achieve fairness in facility closures. So far this effort has led to:
</p>
<div class="square-bullets">
  <ul>
    <li>Three student theses with three published articles.</li>
    <li>Grant funding supporting a postdoctoral researcher to quantify <em>subjective</em> opinions on recycling campaigns and incorporate human perceptions into decision models.
      <span class="inline-toggle" onclick="toggleDetails(this)">[Click for more →]</span>
    </li>
  </ul>
</div>
</div>

    <div class="research_subsection_image">
      <div style="text-align: center; margin-bottom: 0.5em; font-weight: bold;">
        Both the Bavarian government and the Hampshire councils have shut down recycling centers in the past two decades. <br>
        <a href="https://onlinelibrary.wiley.com/doi/10.1002/net.22221" style="color: #0066cc; text-decoration: underline;">Explore →</a>
      </div>
      <img src="/assets/images/recycling.png" alt="Fairness & Waste Management" />
    </div>
  </div>

  <div class="inline-details" style="display: none; margin-top: 1em;">
    <p>This theme is truly interdisciplinary:</p>
    <div class="square-bullets">
      <ul>
        <li><em>Theoretical</em>: Defined new axioms of fairness, shifting the perspective to the facilities themselves. Formulated novel classes of FLPs satisfying axiomatic fairness properties, derived from their Karush–Kuhn–Tucker (KKT) optimality conditions. <a href="https://pubsonline.informs.org/doi/10.1287/ijoc.2022.0308" style="color: #0066cc; text-decoration: underline;">Explore →</a></li>
        <li><em>Computational</em>: Addressed the intractability of solving these models naively by designing specialized algorithms, enabling efficient solutions for large-scale instances at the scale of Bavaria and all of Germany. <a href="https://pubsonline.informs.org/doi/10.1287/ijoc.2024.0693" style="color: #0066cc; text-decoration: underline;">Explore →</a></li>
        <li><em>Societal</em>: Ensured sustainability goals are achieved without disproportionately affecting certain communities by offering governments ethically fair decision-making tools for closing recycling centers while maintaining public accessibility. <a href="https://onlinelibrary.wiley.com/doi/10.1002/net.22221" style="color: #0066cc; text-decoration: underline;">Explore →</a></li>
      </ul>
    </div>
  </div>
</div>

## Pandemic Risk Mitigation

<div class="research_section_wrapper">
  <div class="research_subsection">
    <div class="research_subsection_text">
      <p>
        I began collaborating with the <em>Texas Department of State Health Services</em>, US, as an MSc student in 2012, helping prepare for future pandemics long before the emergence of COVID-19. Motivated by Texas's response to the 2009 H1N1 pandemic, my PhD research focused on designing web-based, optimization-backed decision-support tools for government use. These tools, accessible at <a href="https://flu.tacc.utexas.edu/" style="color: #0066cc; text-decoration: underline;">flu.tacc.utexas.edu</a>, assist the State of Texas in the fair and efficient allocation of critical resources, such as antivirals and vaccines.
      </p>
      <p>
        The most significant funding here is provided by a three-year grant from the <em>Deutsche Forschungsgemeinschaft</em> (German Research Foundation), with additional funding from the <em>Bavarian Czech Academic Agency</em> and the <em>EU Horizon 2020 Program</em>. 
        <span class="inline-toggle" onclick="toggleDetails(this)">[Click for more →]</span>
      </p>
    </div>

    <div class="research_subsection_image">
      <div style="text-align: center; margin-bottom: 0.5em; font-weight: bold;">
        Our collaborative work designed the system of staged lockdowns used by Austin, Texas during COVID-19. <br>
        <a href="https://www.pnas.org/doi/abs/10.1073/pnas.2009033117" style="color: #0066cc; text-decoration: underline;">Explore →</a>
      </div>
      <img src="/assets/images/lockdown.png" alt="Pandemic Risk Mitigation" />
    </div>
  </div>

  <div class="inline-details" style="display: none; margin-top: 1em;">
    <p>During the COVID-19 pandemic, I renewed this collaboration to address pressing challenges in pandemic response. Key contributions include:</p>
    <div class="square-bullets">
      <ul>
        <li><em>Testing Accessibility</em>: Measuring the reach and equity of COVID-19 testing across the United States. <a href="https://link.springer.com/article/10.1007/s10729-020-09538-w" style="color: #0066cc; text-decoration: underline;">Explore →</a></li>
        <li><em>Triggering Lockdowns</em>: Designing the staged-dashboard lockdown system employed by the City of Austin, Texas, which integrates a chance-constrained framework for informed, adaptive public health policies. <a href="https://www.pnas.org/doi/abs/10.1073/pnas.2009033117" style="color: #0066cc; text-decoration: underline;">Explore →</a></li>
      </ul>
    </div>
  </div>
</div>