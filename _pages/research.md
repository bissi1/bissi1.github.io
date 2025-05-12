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

This research represents a *theoretical* interest where I explore joint-chance constraints through the lens of classical probability theory. Specifically, I approach a joint-chance constraint as a union of sets and utilize classical probability bounds to constrain it effectively. Bounding the probability of the union of $n$ events using joint probabilities of $k < n$ events has a rich history, dating back to the foundational work of Boole and Bonferroni. What makes this line of probabilistic research particularly interesting is its application in optimization models. When these probabilistic bounds are incorporated into chance-constrained optimization models, they provide upper and lower bounds on the optimal objective function value, providing both computational and theoretical insights. <a href="#" onclick="this.nextElementSibling.style.display='block';this.style.display='none';return false;" style="color: #0066cc; text-decoration: underline; cursor: pointer;">[Click for more →]</a>

<div id="more-probabilistic-bounds" style="display:none; margin-top: 0.5em;">
The mathematical foundation for this work draws on **large deviations theory**, **concentration inequalities**, and **tail bounds** for heavy-tailed distributions. These tools allow me to quantify the likelihood of extreme outcomes in high-dimensional, uncertain systems, providing critical insights for **risk management** and **system reliability**.
</div>

<div style="display:none; margin-top: 0.5em;"> This interest originated during my PhD studies and matured further following my first major grant as a Principal Investigator during my position at Sandia National Labs, US (2018). The grant from the US Department of Energy supported significant advancements in this domain, culminating in two publications: [here](https://link.springer.com/article/10.1007/s11590-019-01387-z) and a follow-up [here](https://link.springer.com/article/10.1007/s11590-020-01592-1). Currently, this work is being extended collaboratively with my PhD student, focusing on deeper theoretical insights and broader applications. 
</div>

## Sustainability & Climate Change

As countries advance towards Net-Zero goals (e.g., Germany's *Energiewende*), joint chance constraints have proven especially effective for ensuring the highly reliable operation of critical energy systems under uncertain renewable energy availability. Key examples include photovoltaic (PV) systems and coupled wind-diesel systems. Mathematical optimization models for such systems often present significant challenges due to their structure and scale, necessitating the development of novel algorithmic approaches. In my research, we have designed modern *machine-learning inspired* iterative algorithms and employed Lagrangian-based heuristics to tackle these challenges. See examples [here]() and [here]. <a href="#" onclick="this.nextElementSibling.style.display='block';this.style.display='none';return false;" style="color: #0066cc; text-decoration: underline; cursor: pointer;">[Click for more →]</a>

At Sandia National Labs, US (2016–19), I focused on solving large-scale energy system models, addressing critical risks faced by the US electrical grid. Many of these works are available on the US Department of Energy's Office of Scientific and Technical Information's website. Access here →

At FAU Erlangen-Nürnberg, Germany (2019–22), I led the chair’s contributions to the multi-institute “METIS” research collaboration with the Jülich Research Center. This project develops open-source tools for optimizing large-scale energy system models under the framework of Germany’s Energiewende (transition to clean, yet reliable energy systems).

Learn more about the project here →

Explore the technical details here →

This research not only advances mathematical optimization but also contributes to global sustainability goals, ensuring renewable energy systems remain both efficient and reliable under uncertainty.