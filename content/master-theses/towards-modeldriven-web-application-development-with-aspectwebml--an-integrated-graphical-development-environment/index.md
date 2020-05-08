---
authors:
- Gerhard Preisinger
categories: []
date: '2020-05-08 14:38:49+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Towards Model-driven Web Application Development with AspectWebML - An Integrated
  Graphical Development Environment
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in December 2007.

Model Driven Engineering (MDE) and Aspect Oriented Software Development (AOSD) are among what is to be said ’the next big thing’. Despite their youth, both approaches already show their value to the software engineering community manifold and gain more and more attention as well in other domains. For example, in web engineering, some web modeling methodologies have already started to profit from the ideas of MDE and ASOD. Still, the common drawback of most emerging technologies is the inescapable lack of tool support, being especially true for aspect-oriented modeling languages and web modeling languages.

Recently, the web modeling language WebML, an academic method that is supported by the commercial tool WebRatio, has been extended with concepts from the aspect-orientation paradigm. The resulting aspectWebML modeling language, allows for separately modeling crosscutting concerns such as customization for context-aware web applications, from the rest of the applications functionality. Currently aspectWebML is supported by a simple tree-based modeling editor built upon the Eclipse Modeling Framework (EMF), only. While such EMF editors have been around for some time and proved their usefulness, their clumsy handling certainly does not address the modelers‘ needs.

The primary objective of this work is to propose an Graphical Integrated Develoment Environment (IDE) for allowing to develop web applications with aspectWebML in the sense of MDE. In this respect, a major focus is placed on integrating views that support the user in modeling and quickly absorbing aspect-orientation-related interconnections between elements, being at the very core of the aspectWebML language. The concepts of Model-driven Development will be extensivley used throughout all phases of this thesis, starting with the IDE’s major graphical editors parts being created with Eclipses Graphical Modeling Framework (GMF) that allows to quickly craft powerful graphical editors on any EMF-based metamodel. Furthermore, some technologies that build the foundation for GMFs success, i.e. EMF and the code generation framework openArchitectureWare (OAW), are to be used in the next step to construct basic model transformation and code generation facilites for aspectWebML that can be easily plugged into the IDE. The ultimate goal is to show how building an integrated toolset for custom metamodels can be done efficiently with current (open source) technologies.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Preisinger_paper.pdf) and [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Preisinger_poster.pdf)

*Advised by {{% mention "andrea-schauerhuber" %}}, {{% mention "gertrude-kappel" %}}*