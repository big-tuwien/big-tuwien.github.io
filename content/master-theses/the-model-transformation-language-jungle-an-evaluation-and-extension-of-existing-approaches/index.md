---
authors:
- Philipp Huber
categories: []
date: '2020-05-08 15:18:32+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: The Model Transformation Language Jungle - An Evaluation and Extension of Existing
  Approaches
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in May 2008.

Model Transformations are a key-prerequisite for Model Driven Engineering and therefore represent an active research area. Many model transformation languages are available, whereas the languages can be categorized into different approaches. Depending on the particular situation, one model transformation approach might be better suited to accomplish the given task than another approach. Classifications of model transformation languages exist, which also includes a taxonomy of general features a model transformation language may support. Based on this taxonomy, it is possible to compare model transformation approaches in order to find out how suitable they are for a given problem. Like in common object oriented programming approaches, such as Java, there are some particular problems which appear repeatedly. For example, it is often necessary to transform an attribute value in the source model to an object in the target model. For such cases, it should be considered to solve these problems in a generic way. In addition, the generic solutions can be reused in other model transformations.

In this thesis, four model transformation languages, namely ATL, SmartQVT, Kermeta and Triple Graph Grammars (TGG) (using MOFLON as transformation tool) are evaluated based on the taxonomy proposed by Czarnecki et al. These languages are chosen, because the represent the state of the art in model transformation. ATL and SmartQVT are hybrid (a mixture of declarative and imperative) languages. More specifically, SmartQVT implements the „operational“ part of the OMG QVT standard. Kermeta acts as example for an imperative language, whereas TTGs represent a declarative approach with a graphical syntax.

For the purpose of conducting the evaluation, several model transformation examples are defined and implemented using the languages mentioned above. These examples cover model transformation problems appearing in practice, in order to emphasize the advantages and limitations of the particular language. In the second part of this thesis, Kermeta is used to implement a library which solves common problems appearing in model transformations. This library can then be used in practical transformations for simplifying the development process. Finally, the results of the evaluation are interpreted and discussed, in order to propose guidelines on which model transformation approaches are suitable for which problems.

Krzysztof Czarnecki and Simon Helsen. Classification of model transformation approaches. OOPSLA’03 Workshop on Generative Techniques in the Context of Model-Driven Architecture, 2003.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Huber_paper.pdf) and [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Huber_poster.pdf)

*Advised by {{% mention "manuel-wimmer" %}}, {{% mention "gertrude-kappel" %}}*