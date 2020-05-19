---
advisors:
- manuel-wimmer
authors:
- Alexander Eigner
categories: []
date: '2020-05-19 12:37:28+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: 'From Modeling Languages to Query Languages: A Generative Approach'
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

Domain experts often use Domain Specific Languages (DSL) for creating their models. They prefer DSLs over General Purpose Languages (GPL) for the following reasons.  
 Firstly, DSLs are computer languages that are designed to be only used in a particular area of application and to meet as many needs of domain experts of this area as possible.  
 In contrast, GPLs are meant to be used in various domains and are therefore not tailored towards particular areas of application. Hence, domain experts can be confronted with modelling problems that are easily solvable by the means of DSLs but hardly via GPLs.  
 Secondly, domain experts may lack IT-training and can therefore be overwhelmed by the task of learning a particular GPL. They will use a DSL instead, which can be much easier to learn and to apply in the particular modelling domain.  
 Despite of the benefits, the use of a DSL can also lead to some difficulties. Domain Experts need to query their models for all sorts of data.  
 In order to query a model that was designed in a DSL one needs to use a more general query language, which is not perfectly suited to the considered domain and may not be capable to express everything that is necessary.  
 The possibility to have a query language that is already based on the characteristics of the corresponding DSL-model and does not require excessive training of their modellers would be of great use.  
 The aim of this work is to provide a DSL-based query engine, more precisely an EMF-based tool for querying models that are designed in the DSL AutomationML.  
 A transformation engine will be developed, which will handle the generation of the query language’s meta-model based on AutomationML’s meta-model.  
 Afterwards an engine based on VIATRA will be developed to process the queries that were designed in the generated query language.  
 The resulting query engine will be evaluated in terms of efficiency (average query-length,intuitiveness,execution time,…) and effectiveness (amount of supported functions).