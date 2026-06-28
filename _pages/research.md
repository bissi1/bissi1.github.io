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
    <li>Optimization under uncertainty: how to make high-stakes decisions when future information is imperfect?</li>
    <li>Foundations of fairness: how to characterize fairness axiomatically through a model's optimality conditions?</li>
  </ul>
</div>

My research is grounded in mathematical theory but always motivated by real-world challenges. Key application areas include public-health preparedness, infectious disease outbreaks, energy-system planning, sustainability, and resource allocation (details below). Over the past 15 years, I have collaborated with governments, public agencies, and research institutes across the US, Europe, and Asia.

<strong> Selected funding agencies and partners:</strong>
<img src="/assets/images/funding_new.png" alt="Interdisciplinary Research" 
     style="display:block; max-width:90%; max-height:300px; width:auto; height:auto; margin-bottom:1.5rem;">

## Optimization Under Uncertainty

<div class="research_section_wrapper">
  <div class="research_subsection">
    <div class="research_subsection_text">
      <p>
      My specific focus within stochastic optimization is <em>chance-constrained programming</em>, where one must satisfy guaranteed reliability requirements despite uncertain future outcomes. This framework provides a mathematically rigorous way for balancing risk and performance, but the models are often computationally challenging to solve. My work investigates approximations of joint chance constraints. <span class="inline-toggle" onclick="toggleDetails(this)">[Click for more →]</span>      
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
      This research originated during my doctoral studies and was significantly advanced by a US Department of Energy grant to me during my time at Sandia National Laboratories. Here, we develop new bounds for joint chance-constrained models, drawing upon classical probability research dating back to Boole, Bonferroni, and Fréchet. The resulting research contributes to both probability theory and stochastic optimization.
    </p>

    <p>
    Traditional probability union bounds are evaluated by how tightly they approximate the underlying constraint. However, my research demonstrates that stronger theoretical bounds on the constraint do not necessarily yield stronger objective bounds in practice. Or, due to computational limitations, the best approximation of a feasible region may fail to produce the strongest bound on the optimal objective value. Two representative publications include: <a href="https://link.springer.com/article/10.1007/s11590-019-01387-z">this article</a> and <a href="https://link.springer.com/article/10.1007/s11590-020-01592-1">its follow-up</a>.
</p>

    <p>
     My ongoing work, with my PhD student, is extending these ideas to broader stochastic optimization classes.
    </p>
  </div>
</div>

## Sustainability, Energy Systems & Climate Change

<div class="research_section_wrapper">
  <div class="research_subsection">
    <div class="research_subsection_text">
      <p>
      Global transition towards sustainable energy systems presents major optimization challenges. Renewable energy sources (e.g., wind and solar) introduce volatility, while infrastructure planning requires highly reliable operation. My research develops large-scale mathematical models and scalable algorithms for planning & operating energy systems under uncertainty. Particularly, I use chance-constrained optimization with Lagrangian-based approaches and machine-learning-inspired iterative algorithms.
      <span class="inline-toggle" onclick="toggleDetails(this)">[Click for more →]</span>
      </p>

    </div>

    <div class="research_subsection_image">
      <div style="text-align: center; margin-bottom: 0.5em; font-weight: bold;">
        Optimization for reliably integrating renewable energy sources.
        <a href="https://optimization-online.org/2025/09/measuring-the-economic-value-of-wind-solar-complementarity-in-europe-using-chance-constraints/" style="color: #0066cc; text-decoration: underline;">Explore →</a>
      </div>
      <img src="/assets/images/german_energy.png" alt="Sustainability & Climate Change" />
    </div>
  </div>

  <div class="inline-details" style="display: none; margin-top: 1em;">
    <div class="square-bullets">
      <p>
        During my time at Sandia National Laboratories (2016–2019), I worked on large-scale optimization models arising in US energy systems and critical infrastructure. These projects addressed challenges relevant to the resilience and reliability of the US electrical grid under uncertainty. Many resulting reports and publications are publicly available through the US Department of Energy's Office of Scientific and Technical Information website. Access 
          <a href="https://www.osti.gov/search/semantic:bismark%20singh">here →</a>.
      </p>

      <p>
      Then, at FAU Erlangen–Nürnberg (2019–2022), I led the chair's research contributions to the multi-institutional METIS collaboration with Forschungszentrum Jülich, one of Europe's leading energy research centres. This project focused on developing optimization methods and open-source software for large-scale energy-system planning under Germany's <em>Energiewende</em>. Learn more about the METIS project <a href="https://www.fz-juelich.de/en/ice/ice-2/projects/metis?expand=translations,fzjsettings,nearest-institut">here →</a>. Explore the technical details of the ETHOS.FINE package <a href="https://github.com/FZJ-IEK3-VSA/FINE" style="color: #0066cc; text-decoration: underline;">here →</a>.
      </p>
      </div>
    <p>
      Beyond mathematical contributions, this research theme supports governmental goals of designing energy systems that remain reliable, economically viable, and environmentally sustainable in the presence of uncertainty. See this <a href="https://link.springer.com/article/10.1007/s10287-018-0309-x">early</a> and this  <a href="https://link.springer.com/article/10.1007/s10898-021-01041-y">later</a> contribution.
    </p>
  </div>
</div>


## Fairness & Optimization

<div class="research_section_wrapper">
  <div class="research_subsection">
    <div class="research_subsection_text">
     <p>
  A central theme of my research concerns the mathematical foundations of fairness in optimization and econometrics. Rather than imposing fairness as an external design criterion, I investigate how fairness principles can be derived directly from mathematical models and their optimality conditions. This perspective has led to new fairness axioms, optimization formulations, and theoretical characterizations of equitable decision-making. </p>
  <p> These mathematical developments have found applications in undesirable facility location, sustainable waste management, public-health planning, and machine learning. Supported by the Bavarian State Ministry for Science &amp; Arts and internal grants from the University of Southampton, this research has produced several completed student theses, funded postdoctoral researchers, and several published articles. <span class="inline-toggle" onclick="toggleDetails(this)">[Click for more →]</span> </p> </div>

    <div class="research_subsection_image">
      <div style="text-align: center; margin-bottom: 0.5em; font-weight: bold;">
        Declining numbers of recycling centers motivate fair infrastructure planning. <br>
        <a href="https://onlinelibrary.wiley.com/doi/10.1002/net.22221" style="color: #0066cc; text-decoration: underline;">Explore →</a>
      </div>
      <img src="/assets/images/recycling.png" alt="Fairness & Waste Management" />
    </div>
  </div>

  <div class="inline-details" style="display: none; margin-top: 1em;">
    <div class="square-bullets">
      <ul>
        <li><em>Theoretical</em>: Developed new fairness axioms for optimization &amp; econometrics by deriving desirable properties from Karush–Kuhn–Tucker (KKT) optimality conditions rather than prescribing them externally. <a href="https://pubsonline.informs.org/doi/10.1287/ijoc.2022.0308" style="color: #0066cc; text-decoration: underline;">Explore →</a></li>
        <li><em>Computational</em>: Designed specialized algorithms and complexity results for large-scale fairness-aware optimization models, enabling practical solution of instances at the scale of Bavaria and Germany. <a href="https://pubsonline.informs.org/doi/10.1287/ijoc.2024.0693" style="color: #0066cc; text-decoration: underline;">Explore →</a></li>
        <li><em>Societal</em>: Applied these methods to reform recycling-center networks while balancing accessibility and utilization for sustainability objectives. The resulting models provide both <a href="https://onlinelibrary.wiley.com/doi/10.1002/net.70056" style="color: #0066cc; text-decoration: underline;"> Hampshire </a> and <a href="https://onlinelibrary.wiley.com/doi/10.1002/net.22221" style="color: #0066cc; text-decoration: underline;">Bavaria</a> with mathematically grounded decision-support tools for equitable infrastructure planning.</li>
        </ul>
    </div>
  </div>        
</div>         

## Pandemic Risk Mitigation

<div class="research_section_wrapper">
  <div class="research_subsection">
    <div class="research_subsection_text">
      <p>
        I began collaborating with the Texas Department of State Health Services in 2012, helping develop quantitative tools for pandemic preparedness long before the emergence of COVID-19. Motivated by Texas's response to the 2009 H1N1 pandemic, my PhD research focused on designing optimization-based decision-support systems for allocating scarce medical resources such as vaccines, antiviral drugs, and testing facilities.  These efforts led to web-based planning tools, accessible through
        <a href="https://flu.tacc.utexas.edu/" style="color: #0066cc; text-decoration: underline;">flu.tacc.utexas.edu</a>,
        that support state-level decision-making in Texas. During the COVID-19 pandemic, the collaboration expanded to include testing accessibility, healthcare-capacity protection, and staged intervention policies. Our work informed the risk-based alert system adopted by the City of Austin and resulted in publications in <a href="https://www.pnas.org/doi/abs/10.1073/pnas.2009033117" style="color: #0066cc; text-decoration: underline;">PNAS</a>, <a href="https://www.nature.com/articles/s41467-021-23989-x" style="color: #0066cc; text-decoration: underline;">Nature Communications</a>, and <a href="https://link.springer.com/article/10.1007/s10729-020-09538-w" style="color: #0066cc; text-decoration: underline;">other</a> leading journals.
      </p>
      <p>
        My research in this area is supported by the German Research Foundation (DFG), the Bavarian-Czech Academic Agency, and the EU Horizon 2020 program.
        <span class="inline-toggle" onclick="toggleDetails(this)">[Click for more →]</span>
      </p>
    </div>

    <div class="research_subsection_image">
      <div style="text-align: center; margin-bottom: 0.5em; font-weight: bold;">
        Our collaborative work designed Austin's COVID-19 staged-alert system. <br>
        <a href="https://www.pnas.org/doi/abs/10.1073/pnas.2009033117" style="color: #0066cc; text-decoration: underline;">Explore →</a>
      </div>
      <img src="/assets/images/lockdown.png" alt="Pandemic Risk Mitigation" />
    </div>
  </div>

  <div class="inline-details" style="display: none; margin-top: 1em;">
    <p>
      Other selected projects from this research include:
    </p>
    <div class="square-bullets">
      <ul>
        <li>
          <em>Testing Accessibility</em>: Quantifying and improving equitable access to COVID-19 testing facilities across the United States. <a href="https://link.springer.com/article/10.1007/s10729-020-09538-w" style="color: #0066cc; text-decoration: underline;">Explore →</a>
        </li>
        <li>
          <em>Pandemic Influenza Preparedness</em>:
          Optimization models for allocating vaccines and antiviral drugs across public-health distribution networks.
          <a href="https://doi.org/10.1371/journal.pone.0182720"
             style="color: #0066cc; text-decoration: underline;">Explore →</a>
        </li>
      </ul>
    </div>
  </div>
</div>