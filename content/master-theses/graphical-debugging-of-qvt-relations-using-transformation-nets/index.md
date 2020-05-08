---
authors:
- Patrick Zwickl
categories: []
date: '2020-05-08 15:44:59+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Graphical Debugging of QVT Relations using Transformation Nets
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in December 2009.

Model transformations (MT) play a key role in the Model Driven Engineering (MDE) paradigm, leading to the standardization of the Query/View/Transformation (QVT) model transformation language by the Object Management Group (OMG). Until now, however, this language did not attract the same interest as the Unified Modeling Language (UML), because of the lack of adequate debugging facilities which are necessary regarding the following three problem areas: First, declarative languages like QVT Relations (QVT-R) hides the operational semantics of transformations. Only the information provided by the interpreter, as well as the tendered inputs and returned outputs are available for tracking the progress of transformations. Furthermore, the ordering of transformation application is hidden by the MT engines providing only a black-boxes view to the users. This can lead to the problem of impedance mismatches between design and runtime. These characteristics of QVT-R are assets for developing, but are handicaps for debugging. Second, QVT-R code is specified on higher abstraction level than its execution and state-of-the-art debugging. This deteriorates the ability to deduce causes from produced results. Third, the information content responsible for operating MTs is spread over several artifacts including the input model, a resulting target model and the QVT-R code. As a consequence, the reasons for a particular outcome are hard to be derived from the involved artifacts. This severely harms the ease of debugging. Therefore, this master thesis tackles the mentioned problems by visualizing QVT-R as Transformations Nets, using the MT framework „Transformations On Petri Nets In Color“ (TROPIC) based on Colored Petri Nets (CPN). This can be seen as explicit definition of operational semantics on a high abstraction level providing a white-box view for debugging QVT-R. This thesis proposes a procedure model formulated in a conceptual approach and in a prototypic implementation striving for bridging the existing gap between these two different paradigms by mapping the concepts of QVT Relations to such nets. In this thesis three particular contributions are provided: (i) a solution approach for unidirectional mappings producing target models from an existing source model, (ii) the support for model inheritance, (iii) and synchronization approaches for timely and version-based incremental changes.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Zwickl_paper1.pdf) and [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Zwickl_poster1.pdf)

*Advised by {{% mention "johannes-schoenboeck" %}}, {{% mention "gertrude-kappel" %}}*