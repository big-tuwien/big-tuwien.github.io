---
authors:
- Dorian Leroy
- Manuel Wimmer
- Erwan Bousse
categories: []
date: '2020-05-08 18:19:01+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: A Generic White-Box Testing Framework for Model Transformations
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

### Topic

Model transformations are crucial for the success of Model-Driven Engineering (MDE), comparable in role and importance to compilers for programming languages, allowing to transform models between languages and abstraction levels, e.g., to generate platform-dependent models from platform-independent ones. Given their prominent role in MDE and their increasing use in safety critical areas such as the aviation industry, proper means for testing the correctness of model transformations are inevitable.

Although first testing frameworks have been proposed, they fall short with respect to the crucial phases of test source model generation and fault localization, and they are typically hardly configurable and tightly coupled to a certain transformation language. Second, apart of these frameworks, first isolated approaches for the phase of test source model generation have been proposed, which, however, rely mostly on black-box testing techniques, thus, incorporating the source metamodels and the requirements, but neglect the transformation definition, which may lead to untested parts of the transformation definition. Finally, means for fault localization are missing, since testing approaches identify the failing of a test case, but miss to provide the failing parts of the transformation definition.

For tackling these limitations, the aim of this project is to establish a comprehensive testing framework for model transformations called TETRABox (A Generic White-Box TEsting Framework for Model TRAnsformations), whereby we base on the experiences gained in our previous FWF-funded project TROPIC. TETRABox supports all testing phases, ranging from test source model generation to fault localization especially focusing on configurable components. To keep the framework broadly applicable, the envisioned components for testing are independent of a transformation language, allowing new languages to be incorporated by providing a transformation to the common formalism of a control flow graph. Second, to leverage white-box testing, TETRABox allows the automatic generation of test source models on basis of the transformation definition by means of symbolic execution. Finally, for fault localization, oracles offering a dedicated failure trace are employed, which are used to provide an entry point for debugging by slicing techniques.

The methodology for evaluating the TETRABox framework builds on three major pillars. First, transformations of the ATL model transformation zoo will be systematically tested by means of mutation testing and the results will be compared to existing testing techniques. Second, an empirical study with students from our model engineering courses (around 200 master students every year) will be conducted, whereby errors will be seeded into existing transformations, and the students will have to spot these errors with and without the help of the TETRABox framework. Finally, dedicated workshops will be held with (inter-)national partners.

More information here:&nbsp;<http://modeltransformation.net/tetrabox/>

### Term

01.08.2016 - 28.02.2019

### Funding

Austrian Science Fund (FWF), grant number P28519-N31