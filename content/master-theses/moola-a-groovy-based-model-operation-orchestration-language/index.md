---
advisors:
- manuel-wimmer
authors:
- Stefan Weghofer
categories: []
date: '2020-05-11 21:33:24+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Moola - A Groovy-based Model Operation Orchestration Language
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

A core concept of Model-Driven Software Engineering (MDSE) is the use of models and transformations. Models represent information of the system, while transformations allow converting one or more input models to specific output models. In the last years, more and more transformation languages were introduced to allow MDSE to be applied to a wide spectrum of use cases. Today, many advanced scenarios can be expressed by MDSE and the use of new transformation languages. However, in every non-trivial project, multiple transformations have to be executed in particular order to yield the final result. Most transformation languages do not allow to be integrated in such an orchestration. They either lack interfaces to the outside and hence violate the black box principal or need a specific execution context, such as a running development environment. In this thesis, I analyze several existing tools for Transformation Orchestration, which try to overcome these problems to allow for the orchestration of various transformation languages to one transformation chain. I then take inspiration from these tools and other domains, such as Build Management and Workflow Management, to create a new tool for Transformation Orchestration called Moola. Especially concepts from build tools such as Gradle can be applied to Transformation Orchestration. If we see the models of the last transformation as overall outcome, the whole orchestration can be seen as build process. Like Gradle, Moola will be implemented as domain-specific language in Groovy. This allows for powerful, yet easy to read orchestration mark-up. Moola will then be evaluated against use cases taken from the ARTIST project.