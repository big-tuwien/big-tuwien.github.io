---
authors:
- Assad Lodhi
categories: []
date: '2020-05-08 15:18:33+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: ProfileGen - Ein Eclipse Plugin für Interoperabilität zwischen DSML und UML
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in February 2011.

Current software development projects comprise the development of complex software systems under immense time pressure. In the past decade, model-driven software development (MDSD) has become mainstream to tackle these challenges. In MDSD, domain specific modelling languages (DSML) are becoming more and more important. These languages allow to concisely represent all the peculiarities of a given domain in a model. But being so specific, interoperability is needed with standardized modeling languages such as UML, because they offer a more common way of communication between different stakeholders. At the moment, interoperability can only be achieved by manually creating transformations between DSMLs and UML which is a challenging task.

This thesis presents a tool named ProfileGen, which tackles this challenge by proposing a semi-automatic approach for generating such transformations needed for interoperability between DSMLs and UML. In particular, a mapping language is presented which allows to manually link DSML elements with UML elements on a high-level of abstraction. From such mappings, a generator framework automatically creates all artifacts needed for interoperability, including transformations from the DSMLs to UML and vice versa, as well as UML profiles for ensuring information loss free transformations .The approach is evaluated by a real-world case study, namely integrating WebML (a DSML for data-intensive Web applications) with UML.

&nbsp;

*Advised by {{% mention "manuel-wimmer" %}}, {{% mention "gertrude-kappel" %}}*