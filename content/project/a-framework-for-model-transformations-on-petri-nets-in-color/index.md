---
authors:
- Johannes Schönböck
- Manuel Wimmer
- Gertrude Kappel
categories: []
date: '2020-05-08 21:22:07+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: A Framework for Model Transformations on Petri Nets in Color
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

### Topic

Model transformations play an important role in software engineering in general and in the area of model-driven engineering in particular, representing the key mechanisms for model translations (e.g., translating an ER model into a UML class model), model augmentations (e.g., weaving aspects into a UML class model), and model alignments (e.g., mapping a content model to its GUI view), to mention just a few. Several kinds of dedicated model transformation languages have emerged during the last years, which allow specifying and executing transformations between source and target metamodels and their corresponding models, respectively. However, none of these languages, not even the QVT-standard proposed by the OMG, became generally accepted as a state-of-the-art technology for model transformations. This rare adoption of model transformation languages in practice is due to several reasons. First, existing model transformation languages do not provide appropriate abstraction mechanisms to deal with the complexity of structural heterogeneities of different metamodels. Second, they lack suitable reuse mechanisms in order to reduce the high and error-prone effort of specifying recurring transformations. And finally, these languages exhibit an inherent impedance mismatch between the specification and the execution of model transformations in terms of a one-to-many derivation of concepts, thus hampering both, understandability and debuggability. The aim of this project is to establish a framework called TROPIC (Transformations on Petri Nets in Color) for developing model transformations which tackles these limitations. First, TROPIC allows to specify model transformations on different abstraction levels, providing both a declarative mapping language based on UML 2 component diagrams which hides implementation details, and derived from that, an executable transformation language using Coloured Petri Nets. Second, TROPIC facilitates reusability by providing an initial library of generic transformation operators which can be bound to arbitrary metamodels and by allowing to extend this library on demand with new, user-defined, transformation operators, optionally composed out of already existing ones. Finally, TROPIC overcomes the impedance mismatch by supporting a dedicated runtime model in terms of Coloured Petri Nets, allowing for a homogeneous representation of all transformation artefacts (i.e., models, metamodels and the transformation logic itself), which fosters understandability and debuggability of model transformations. The methodology for evaluating the proposed framework builds on three major pillars. First, appropriate case studies for transforming heterogeneous structural as well as behavioural models will be set up and implemented with different existing model transformation languages, including TROPIC, the results being evaluated on basis of a suitable subset of the ISO 9126 software quality model. Second, the findings of these case studies will be further critically reflected by conducting an empirical study with students from our model engineering courses (around 200 master students every year). Third, dedicated workshops will be held together with internationally renowned inventors of other model transformation languages to additionally review the value of our proposed framework.

More information: <http://www.modeltransformation.net/>

### Term

01.03.2009 - 31.08.2012

### Funding

Austrian Science Fund (FWF) under grant P21374-N13

### Partner

<ul class="partnerList"><li><a href="http://www.daimi.au.dk">University of Aarhus, Dänemark</a></li><li><a href="http://www.es.tu-darmstadt.de/">Darmstadt University of Technology, Deutschland</a></li><li><a href="http://www.jku.at/">Johannes Kepler Universität Linz, Österreich</a></li><li><a href="http://www.univ-nantes.fr">Université de Nantes, Frankreich</a></li></ul>