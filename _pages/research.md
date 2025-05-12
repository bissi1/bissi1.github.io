---
title: "Interdisciplinary Research"
permalink: /research/
layout: single
classes: full
---

My primary research interest is advancing data-driven decision-making under uncertainty, with a particular focus on two-stage stochastic optimization. My approach balances theoretical novelty with impact-based application, addressing complex societal and environmental challenges via large-scale mathematical models. These models often require the development of specialized algorithms to enable computationally efficient solutions. 

My theoretical research is motivated by two key themes:

- **Chance-constrained optimization** : Designing systems systems resilient to extreme risk conditions. I develop algorithms and approximations that are computationally tractable yet ensuring the critical systems remains safeguarded against rare but catastrophic disruptions. 

- **Optimality conditions of fairness**: I am interested in different axiomatic definitions of fairness and continuous or discrete optimization models that achieve those. For this, I explore the Karush-Kuhn-Tucker conditions of the optimization models.

My interdisciplinary research is motivated by three key applications:

- **Energy Systems**: Designing resilient and sustainable energy infrastructures capable of withstanding uncertain demand, supply fluctuations, and extreme weather events.

- **Pandemic Response**: Developing data-driven models to guide healthcare policy, optimize resource allocation, and ensure fairness in the distribution of scarce medical supplies.

- **Sustainable Waste Management**: Optimizing the placement of recycling centers and waste processing facilities to minimize environmental impact and reduce logistical costs.

A unique aspect of my approach is modeling **subjective human behavior** within the decision-making process. This adds a layer of complexity and realism to my models, bridging the gap between mathematical rigor and human-centric decision-making. 

## Probabilistic Bounds

<div class="probability-section">
  <div class="probability-text">

This research represents a *theoretical* interest where I explore joint-chance constraints through the lens of classical probability theory. Specifically, I approach a joint-chance constraint as a union of sets and utilize classical probability bounds to constrain it effectively. Bounding the probability of the union of $n$ events using joint probabilities of $k < n$ events has a rich history, dating back to the foundational work of Boole and Bonferroni. What makes this line of probabilistic research particularly interesting is its application in optimization models. When these probabilistic bounds are incorporated into chance-constrained optimization models, they provide upper and lower bounds on the optimal objective function value, providing both computational and theoretical insights. 

<details>
  <summary style="color: #0066cc; cursor: pointer;">[Click for more →]</summary>
  
  This interest originated during my PhD studies and matured further following my first major grant as a Principal Investigator during my position at Sandia National Labs, US (2018). The grant from the US Department of Energy supported significant advancements in this domain, culminating in two publications: <a href="https://link.springer.com/article/10.1007/s11590-019-01387-z">this paper</a> and a follow-up <a href="https://link.springer.com/article/10.1007/s11590-019-01387-z">follow-up paper</a>. Currently, this work is being extended collaboratively with my PhD student, focusing on deeper theoretical insights and broader applications. 
</details>
</div>



  <div class="probability-image">
    <div style="text-align: center; margin-bottom: 0.5em; font-weight: bold;">
      Satisfying a joint chance constraint is an intersection of "successes". <a href="https://link.springer.com/article/10.1007/s11590-019-01387-z" style="color: #0066cc; text-decoration: underline;">Explore →</a>
    </div>
    <img src="/assets/images/venn_diagram.png" alt="Probabilistic Bounds" />
  </div>
</div>


## Sustainability & Climate Change

As European countries advance towards **Net-Zero** goals (e.g., Germany's *Energiewende*), joint chance constraints have proven especially effective for ensuring the highly reliable operation of critical energy systems under uncertain renewable energy availability. Key examples include photovoltaic (PV) systems and coupled wind-diesel systems. Mathematical optimization models for such systems often present significant challenges due to their structure and scale, necessitating the development of novel algorithmic approaches. In my research, we have designed modern *machine-learning inspired* iterative algorithms and employed Lagrangian-based heuristics to tackle these challenges. See [this older paper](https://link.springer.com/article/10.1007/s10287-018-0309-x) and [this newer paper](https://link.springer.com/article/10.1007/s10898-021-01041-y). 


<details>
  <summary style="color: #0066cc; cursor: pointer;">[Click for more →]</summary>

At Sandia National Labs, US (2016–19), I focused on solving large-scale energy system models, addressing critical risks faced by the US electrical grid. Many of these works are available on the US Department of Energy's Office of Scientific and Technical Information's website. Access <a href="https://www.osti.gov/search/semantic:bismark%20singh">here →</a>.<br><br>

At FAU Erlangen-Nürnberg, Germany (2019–22), I led the chair’s research contributions to the multi-institute ``METIS" research collaboration with the Jülich Research Center. This project develops open-source tools for optimizing large-scale energy system models under the framework of Germany's <em>Energiewende</em> (transition to clean, yet reliable energy systems).<br>
  
  <ul>
      <li> Learn more about the METIS project <a href="https://www.fz-juelich.de/en/ice/ice-2/projects/metis?expand=translations,fzjsettings,nearest-institut">here →</a>.</li>
      <li> Explore the technical details of the ETHOS.FINE package <a href="https://github.com/FZJ-IEK3-VSA/FINE">here →</a>.</li>
  </ul>

This research not only advances mathematical optimization but also contributes to global sustainability goals, ensuring renewable energy systems remain both efficient and reliable under uncertainty.
</details>


## Fairness & Waste Management

In 2020, I began exploring undesirable facility location problems (FLPs) with a unique perspective: ensuring fairness from the point of view of the facilities, rather than the users, which is the typical approach in existing literature. These models have significant applications in waste management, particularly in the context of **recycling centers** (e.g., UK *tips* or German *Wertstoffhöfe*). Recycling centers, which allow populations to dispose of certain recyclable waste, are critical for achieving sustainability goals. However, they also contribute to pollution and public nuisance, leading many governments to consider their closure. How can such decisions be made ethically and fairly? 

Supported by the **Bavarian State Ministry for Science & Arts** and the **University of Southampton**, my team developed discrete optimization models that achieve fairness in facility closures. Key milestones include:

 <ul>
      <li> Supervising two student theses on this topic, resulting in published articles.</li> 
      <li> Leading a postdoctoral researcher in quantifying subjective opinions on recycling campaigns, incorporating human perceptions into decision models.</li> 

<details>
  <summary style="color: #0066cc; cursor: pointer;">[Click for more →]</summary>

Theoretical: Defined new axioms of fairness, shifting the perspective to the facilities themselves. Formulated novel classes of FLPs with interesting mathematical properties, particularly in their Karush-Kuhn-Tucker (KKT) optimality conditions. Explore→

Computational: Addressed the intractability of solving these models naively by designing specialized algorithms, enabling efficient solutions for large-scale instances of the size of Bavaria and all of Germany. Explore→ 

Societal: Ensured sustainability goals are achieved without disproportionately affecting certain communities by offering governments ethically fair decision-making tools for closing recycling centers while maintaining public accessibility. Explore→  