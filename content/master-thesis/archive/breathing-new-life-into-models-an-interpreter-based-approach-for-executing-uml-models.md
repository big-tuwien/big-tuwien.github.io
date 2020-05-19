---
advisors:
- manuel-wimmer
- gertrude-kappel
authors:
- Tanja Mayerhofer
categories: []
date: '2020-05-19 12:37:42+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: 'Breathing New Life into Models: An Interpreter-Based Approach for Executing
  UML Models'
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in May 2011.

Over the past years the development paradigm Model-Driven Development (MDD) gained significant in popularity. With the usage of this paradigm the software engineering process becomes more model-centric and less code-centric. This means that models become the main artifact in the software development process and therewith the whole software development process relies on these models and their correctness. For this reason the need for executable models that can be tested and validated arose. The Model Driven Architecture (MDA) is the MDD approach developed by the Object Management Group (OMG) that relies on the usage of a bunch of OMG standards. This approach designates the usage of UML to define a platform-independent model of the system that should be developed. The problem is that UML models are not executable because UML has no precise and complete specified semantics. Its semantics is defined informally in English prose and this definition is scattered throughout the standard which is about 1000 pages. Because of this ambiguities arise and models can be interpreted and executed in different ways. This also led to the development of execution tools that are not interoperable because they implement different execution semantics.

&nbsp;

OMG recognized the need for executable models and the corresponding issues with UML and developed a new standard called Semantics of a Foundational Subset of Executable UML Models or foundational UML (fUML) that was released in February 2011. This standard defines the precise execution semantics of a selected subset of UML 2, the so-called foundational UML subset.

&nbsp;

The research question of this thesis is as follows. Is the semantics definition of the fUML standard sound and applicable for building tools that enable the execution of UML activity diagrams? To answer this question, a prototype of a model-interpreter has been developed in this thesis that is able to execute and debug UML models according to the execution semantics defined in the fUML standard. This model-interpreter prototype focuses on executing activity diagrams that model the manipulation of objects and links in a system. Furthermore, the prototype provides reasonable debugging functionality similar to the functionality offered for debugging code like the step-wise execution and the displaying of the debugging progress. The experiences gained during the implementation of the model-interpreter prototype were reflected in order to evaluate the fUML standard itself as well as its applicability. The main conclusion of this evaluation is that the fUML standard is applicable for implementing tools that support the execution of UML activity diagram, but that high efforts are necessary to develop a user-friendly and efficiently usable tool supporting features like the debugging of models or the execution of incomplete models.

Abstract and paper may be found in our <a class="external" href="http://publik.tuwien.ac.at/showentry.php?ID=196765&amp;lang=2">publication database</a>.

 Download the [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Mayerhofer_poster.pdf)