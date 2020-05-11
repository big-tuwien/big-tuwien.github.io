---
advisors:
- manuel-wimmer
- gertrude-kappel
authors:
- Johannes Schoenboeck
categories: []
date: '2020-05-11 21:33:32+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Testing and Debugging of Model Transformations
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in December 2011.

Model-Driven Engineering (MDE) proposes an active use of models to conduct the different phases of software development. The major vision is a shift from the idea of “everything is an object” in the object-oriented paradigm to the idea of “everything is a model” in MDE. Following this vision, it becomes obvious that transformations between models play a key role. Just like any other software, transformations should be engineered using sound and robust engineering techniques. However, current engineering techniques focus on the implementation phase of transformations, but fail to provide means for the analysis, design, testing and debugging phases.

In particular, to support the analysis and design phase, means are needed that allow to formally describe the requirements of a certain transformation in order to allow for automatic validation in the testing phase. In case of a failure, additional means are needed to efficiently debug model transformations. However, current transformation languages provide only scarce support for debugging. This is mainly due to the fact that low-level information of an according execution engine is provided only, e.g., variable values. Finally, the operational semantics is hidden by these execution engines, which further aggravates finding failures and hampers understanding of transformation specifications.

To tackle the aforementioned limitations, this thesis provides three main contributions. First, a declarative, visual language called PAMOMO is proposed, which allows to formally specify requirements on model transformations by means of contracts. To test if a model transformation fulfills the specified requirements, the contracts are compiled into check-only QVT Relations, providing dedicated error traces in case a contract fails. These traces may then be used as hints for debugging. To support debugging, Transformation Nets as a DSL on top of CPNs are proposed, which provide a dedicated runtime model for model transformations, making the hidden operational semantics explicit as a second major contribution. Finally, based on this runtime model various means of debugging are presented as a third contribution.

To evaluate the contributions, relations to competing approaches are drawn in a first step. Second, case studies are used to show the applicability of the presented approaches. To evaluate the runtime model, the operational semantics of dedicated transformation languages is made explicit in terms of Transformation Nets. Finally, the debugging support is evaluated again by case studies and a first user study.

Abstract and paper may be found in our <a class="external" href="http://publik.tuwien.ac.at/showentry.php?ID=209018&amp;lang=2">publication database</a>.