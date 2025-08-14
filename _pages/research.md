---
title: "Interdisciplinary Research"
permalink: /research/
layout: archive
classes: full
---

My primary research interest is advancing <strong>data-driven decision-making under uncertainty</strong>, with a particular focus on two-stage stochastic optimization. My approach balances theoretical novelty with application-driven impact, addressing complex <strong>societal</strong> and <strong>environmental</strong> challenges through the creative development of mathematical models. These models are often large-scale, typically requiring the design of specialized algorithms to enable computationally efficient solutions.

One central focus of my research is <strong>chance-constrained optimization</strong>, where the goal is to design systems that remain resilient even under extreme risk conditions. I work on developing specialized algorithms to solve such stochastic programs, ensuring both tractability and practicality. A second recurring theme is the development of new axiomatic definitions of fairness. Here, I seek to design continuous or discrete optimization models whose Karush–Kuhn–Tucker (KKT) optimality conditions lead to these fairness notions.

### Motivations and Applications
My work is inherently <em>interdisciplinary</em>, driven by real-world challenges such as:
<div class="square-bullets">
  <ul>
    <li><strong>Energy Systems</strong>: Designing resilient and sustainable energy infrastructures under uncertain demand and supply.</li>
    <li><strong>Pandemic Response</strong>: Guiding healthcare policy to ensure fairness across populations and allocate scarce resources effectively.</li>
    <li><strong>Critical Risk Management</strong>: Minimizing the socioeconomic impact of unforeseen man-made attacks or natural disasters.</li>
    <li><strong>Sustainable Waste Management</strong>: Developing models for the efficient placement of recycling centers to promote environmental sustainability.</li>
  </ul>
</div>

A unique aspect of my approach is modeling <strong>subjective human behavior</strong> within the decision-making process. This adds both complexity and realism to my models, bridging the gap between mathematical rigor and human-centric decision-making.

## Probabilistic Bounds

<div class="research_section_wrapper">
  <div class="research_subsection">
    <div class="research_subsection_text">
      <p>
        This research represents a purely theoretical interest, in which I explore joint-chance constraints through the lens of <em>classical probability theory</em>. Specifically, I approach a joint-chance constraint as a union of sets and utilize classical probability bounds to constrain it effectively. Bounding the probability of the union of <em>n</em> events using joint probabilities of <em>k &lt; n</em> events has a rich history, dating back to the foundational work of Boole and Bonferroni.
      </p>
      <p>
        What makes this line of probabilistic research particularly interesting is its application in optimization models. When these probabilistic bounds are incorporated into chance-constrained optimization models, they provide upper and lower bounds on the optimal objective function value, offering both computational and theoretical insights. <span class="inline-toggle" onclick="toggleDetails(this)">[Click for more →]</span>
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
      This interest originated during my PhD studies and matured further following my first major grant as Principal Investigator during my position at Sandia National Labs, US (2018). The grant from the US Department of Energy supported significant advancements in this domain, culminating in
      <a href="https://link.springer.com/article/10.1007/s11590-019-01387-z">this paper</a> and a
      <a href="https://link.springer.com/article/10.1007/s11590-020-01592-1">follow-up paper</a>.
    </p>
    <p>
      Currently, this work is being extended collaboratively with my PhD student, focusing on deeper theoretical insights for bounding two-stage stochastic optimization models.
    </p>
  </div>
</div>

## Sustainability & Climate Change

<div class="research_section_wrapper">
  <div class="research_subsection">
    <div class="research_subsection_text">
      <p>
        As several countries advance towards <strong>Net-Zero</strong> goals (e.g., Germany's <em>Energiewende</em> or France's <em>Transition Énergétique</em>), joint chance constraints have proven especially effective for ensuring highly reliable operation of critical energy systems under uncertain renewable energy availability, such as photovoltaic (PV) systems and coupled wind–diesel systems. Mathematical optimization models for such systems often present significant challenges due to their (a) structure and (b) scale, necessitating the development of heuristics and algorithms.
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
        <li>At Sandia National Labs, US (2016–19), I focused on solving large-scale energy system models, addressing critical risks faced by the US electrical grid. Many of these works are available on the <strong>US Department of Energy's</strong> Office of Scientific and Technical Information website. Access 
          <a href="https://www.osti.gov/search/semantic:bismark%20singh">here →</a>.
        </li>
        <li>At FAU Erlangen–Nürnberg, Germany (2019–22), I led the chair’s research contributions to the multi-institute <code>METIS</code> research collaboration with the <strong>Jülich Research Center</strong>. This project develops open-source tools for optimizing large-scale energy system models under the framework of Germany's <em>Energiewende</em>.
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
        In 2020, I began exploring <strong>undesirable facility location problems</strong> (FLPs) with a unique perspective: ensuring fairness from the point of view of the facilities, rather than the users, which is the typical approach in existing literature. Motivated by applications in waste management, particularly in the context of <strong>recycling centers</strong> (e.g., UK <em>tips</em> or German <em>Wertstoffhöfe</em>), I lead a diverse team of researchers on this subtopic.
      </p>
      <p>
        Supported by the <strong>Bavarian State Ministry for Science & Arts</strong> and the <strong>University of Southampton</strong>, my team develops discrete optimization models that achieve fairness in facility closures. So far this effort has led to:
      </p>
      <div class="square-bullets">
        <ul>
          <li>Two student theses (third ongoing) with three published articles.</li>
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
        I began collaborating with the <strong>Texas Department of State Health Services</strong>, US, as an MSc student in 2012, helping prepare for future pandemics long before the emergence of COVID-19. Motivated by Texas's response to the <strong>2009 H1N1 pandemic</strong>, my PhD research focused on designing web-based, optimization-backed decision-support tools for government use. These tools, accessible at <a href="https://flu.tacc.utexas.edu/" style="color: #0066cc; text-decoration: underline;">flu.tacc.utexas.edu</a>, assist the State of Texas in the fair and efficient allocation of critical resources, such as antivirals and vaccines.
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