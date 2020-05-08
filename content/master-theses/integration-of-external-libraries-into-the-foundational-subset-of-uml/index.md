---
authors:
- Patrick Neubauer
categories: []
date: '2020-05-08 15:28:10+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Integration of External Libraries into the Foundational Subset of UML
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in February 2014.

With the introduction of OMG’s Foundational UML (fUML) standard, that precisely defines the execution semantics for a subset of UML, and the conforming virtual machine, completely executable systems can be built and executed with UML. However, the full potential of having executable models has yet to be unleashed. An important aspect that increases the potential of executable models is the ability to re-use existing software components since that reportedly increases the overall quality and productivity of the software development process. Furthermore, large-scale software that is produced nowadays, involves the usage of a high number of existing software components primarily in form of software libraries (i.e., APIs provided for the used programming language).

This thesis identified that the fUML standard does not offer a procedure to use software libraries. In fact, creating models that build on top of software libraries is not foreseen in the fUML standard. On the contrary, the standard foresees its extendability through the Foundational Model Library. Yet, doing so requires implementing model libraries that basically mimic the functionality provided by currently existing software libraries. This approach imposes a significant drawback. It requires a huge amount of dedicated joint effort to build a set of libraries having similar functional coverage and sophistication as the existing set of software libraries.

The research question of this thesis is as follows. Is the fUML virtual machine extendable, such that it allows the execution of models referencing external software libraries? Within this work, an approach has been elaborated that enables to use external software libraries in fUML models. The applicability of this approach has been shown by implementing a prototypical Integration Layer that is able to integrate Java libraries with the fUML virtual machine such that the modeler can benefit from the advanced and complex functionalities provided by those libraries. This prototype focuses on creating instances of library classes and calling library operations. Moreover, a two-step procedure to make existing libraries available for their usage in fUML models, has been implemented.

While conducting several case studies, experiences have been gained that led to further enhancements of the prototype and to the following conclusion. The fUML virtual machine can be extended, such that it allows the execution of models referencing external libraries. Nevertheless, to broaden the applicability of the implemented prototype, and therefore increase the scope of applicable modeling scenarios, an in-depth investigation on common library use cases and their following implementation is recommended.

Abstract and paper may be found in our <a class="external" href="http://publik.tuwien.ac.at/showentry.php?ID=227306&amp;lang=2">publication database</a>.

 Download the [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Neubauer_poster.pdf)

*Advised by {{% mention "philip-langer" %}}, {{% mention "tanja-mayerhofer" %}}, {{% mention "gertrude-kappel" %}}*