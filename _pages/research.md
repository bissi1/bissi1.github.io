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
        Global transition towards sustainable energy systems presents some of the most challenging optimization problems currently facing society. Renewable energy sources (e.g., wind and solar) introduce volatility, while large-scale infrastructure planning requires reliability. My research develops mathematical models and computationally scalable algorithms for planning and operating energy systems under uncertainty. The mathematical challenge here is due to both the problem's scale and structure. 
      </p>
      <p>
        My focus is on chance-constrained optimization models to ensure highly reliable system performance despite uncertainty in energy generation and/or demand. I am especially motivated by Lagrangian-based methods,  specialized algorithms, and machine-learning-inspired iterative methods to solve practical-scale problems. See this 
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
      <p>
        During my time at Sandia National Laboratories (2016–2019), I worked on large-scale optimization models arising in US energy systems and critical infrastructure. These projects addressed challenges relevant to the resilience and reliability of the US electrical grid under uncertainty. Many resulting reports and publications are publicly available through the US Department of Energy's Office of Scientific and Technical Information website. Access 
          <a href="https://www.osti.gov/search/semantic:bismark%20singh">here →</a>.
      </p>

      <p>
      Then, at FAU Erlangen–Nürnberg (2019–2022), I led the chair's research contributions to the multi-institutional METIS collaboration with Forschungszentrum Jülich, one of Europe's leading energy research centres. This work focuses on developing optimization methods and open-source software for large-scale energy-system planning under Germany's <em>Energiewende</em>. Learn more about the METIS project <a href="https://www.fz-juelich.de/en/ice/ice-2/projects/metis?expand=translations,fzjsettings,nearest-institut">here →</a>. Explore the technical details of the ETHOS.FINE package <a href="https://github.com/FZJ-IEK3-VSA/FINE" style="color: #0066cc; text-decoration: underline;">here →</a>.
      </p>
      </div>
    </div>
    <p>
      Beyond mathematical contributions, this research theme supports governmental goals of designing energy systems that remain reliable, economically viable, and environmentally sustainable in the presence of uncertainty.
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