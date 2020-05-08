---
authors:
- Philip Langer
categories: []
date: '2020-05-08 18:02:37+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Adaptable Model Versioning based on Model Transformation By Demonstration
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in December 2011.

_Model-driven engineering_ (MDE) is evermore adopted in academia and industry for being a new paradigm helping software developers to cope with the ever increasing complexity of software systems being developed. In MDE, software models constitute the central artifacts in the software engineering process, going beyond their traditional use as blueprints, and act as the single source of information for automatically generating executable software.

Although MDE is a promising approach to master the _complexity_ of software systems, so far it lacks proper concepts to deal with the ever growing _size_ of software systems in practice. Developing a large software system entails the need for a large number of collaborating developers. Unfortunately, _collaborative development of models_ is currently not sufficiently supported. Traditional versioning systems for code fail for models, because they treat models just as plain text files and, as a consequence, neglect the graph-based nature of models.

A few dedicated _model versioning approaches_ have been proposed, which directly operate on the models and not on the models‘ textual representation. However, these approaches suffer from four major deficiencies. First, they either support only one modeling language or, if they are _generic_, they do not consider important specifics of a modeling language. Second, they do not allow the specification of _composite operations_ such as refactorings and thus, third, they _neglect_ the importance of respecting the original intention behind composite operations for detecting conflicts and constructing a merged model. Fourth, the types of _detectable conflicts_ among concurrently applied operations is _insufficient_ and _not extensible by users_.

To tackle these deficiencies, we present four major contributions in this thesis. First, we introduce an _adaptable model versioning framework_, which aims at combining the advantages of two worlds; the proposed framework is generic and offers out-of-the-box support for _all modeling languages_ conforming to a common meta-metamodel, but also allows to be _adapted_ for enhancing the versioning support for _specific modeling languages_. Second, we propose a novel technique, called _model transformation by demonstration_, for easily specifying composite operations. Besides being executable, these composite operation specifications also constitute the _adaptation artifacts_ for enhancing the proposed versioning system. More precisely, with our third contribution, we present a novel approach for _detecting applications of specified composite operations_ without imposing any dependencies on the employed modeling environment. Fourth, we present a novel approach for detecting _additional types of conflicts_ caused by _concurrently applied composite operations_. Furthermore, we contribute additional techniques for revealing potentially obfuscated or unfavorable merge results. Besides introducing the contributions from a conceptual point of view, we provide an open source implementation of these concepts and present empirical case studies and experiments for evaluating their usefulness and ease of use.

Download the [slides](http://www.slideshare.net/PhilipLanger/adaptable-model-versioning-using "Slides on Slideshare")

Abstract and paper may be found in our <a class="external" href="http://publik.tuwien.ac.at/showentry.php?ID=203931&amp;lang=2">publication database</a>.

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Langer_P.pdf)

*Advised by {{% mention "martina-seidl" %}}, {{% mention "manuel-wimmer" %}}, {{% mention "gertrude-kappel" %}}*