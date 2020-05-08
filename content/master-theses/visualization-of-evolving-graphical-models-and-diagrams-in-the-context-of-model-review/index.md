---
authors:
- Florian Zoubek
categories: []
date: '2020-05-08 15:28:17+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Visualization of Evolving Graphical Models and Diagrams in the Context of Model
  Review
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

Source code review tools are part of many large scale software development processes. An example for such a code review tool is Gerrit which is used in popular open source projects such as the Android Open Source Project, Eclipse, LibreOffice and many others. Code reviews aim at finding and preventing mistakes introduced by changed artifacts before they are merged into the actual software project. The actual form of such a review varies and ranges from pair programming to formal inspections. However, the basic review process supported by most of the review tools is as follows: The review process is started by a contributor who provides one or more new or modified artifacts to the project. One or more reviewers provide feedback, leave comments on the contribution and decide whether the contribution will be accepted to be merged into the project or not. If not, the contributor may provide new versions of these artifacts based on the feedback of the reviewers and the process starts over again.

This process requires to keep track of the changes introduced to the artifacts and previous feedback, which together form a review history. To support this, most of the source code review tools provide visualization of differences among the changed artifacts and additional annotations, such as comments tied to a specific scope of the text data. However, to the best of our knowledge, these visualizations only support textual artifacts, such as source code. Apart from binary artifacts, this way of visualization is also a problem for artifacts that encode data with text, but are hard to read for humans, such as models and diagrams.

In Model-Driven Engineering, models are the most important artifacts of a software project. Such models are represented by a textual syntax or a graphical syntax. The previously mentioned visualizations are dedicated to show differences between textual artifacts and are hence suitable for models with a textual syntax. However, they do not support models using a graphical syntax, unless they can be encoded in text. Although the latter is technically possible, it is desirable to visualize the changes and annotations using the graphical representation, as this overcomes the burden of learning another representation and keeping them in sync.

The aim of this thesis is to develop a set of visualization techniques to visualize graphical models in the context of review processes. Prototype implementations of the resulting techniques and case studies will be used to verify the results. These prototypes will be built on top of popular open source frameworks and tools used in Model-Driven Engineering, such as Eclipse, and the Eclipse Modeling Framework.

&nbsp;

*Advised by {{% mention "philip-langer" %}}, {{% mention "tanja-mayerhofer" %}}, {{% mention "gertrude-kappel" %}}*