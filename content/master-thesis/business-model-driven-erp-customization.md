---
advisors:
- dieter-mayrhofer
- christian-huemer
authors:
- Thomas Gürth
categories: []
date: '2020-05-19 12:37:31+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Business Model Driven ERP Customization
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in January 2014.

Enterprise Resource Planning (ERP) systems encompass the administration of all resources that are needed for companies to run their business. They support several functional areas, like accounting, manufacturing, and sales in form of modules that are integrated by a single database where all business relevant information is stored. In order to guarantee a flawless and productive use of the system, the economic phenomena underlying the business of the company need to be reflected in the user interface as well as the data structure itself. Usually ERP-systems are purchased by customers from vendors in form of standard software. Such software supports a predefined set of functionality and has to be further customized to the specific needs of an enterprise, which is not a trivial task and often leads to additional costs. Furthermore standard software only supports specific processes that are based on best-practice assumptions of the vendors. Therefore adjusting ERP-systems to changed market demands is hard, since they are missing a business semantic base. Often changed business needs can only be represented by drastic changes in the data structure or the code which can lead to inconsistencies.

The REAlist project uses a model-driven approach to overcome the aforementioned problems with existing ERP-systems, and enhance their adaptability. Business needs can be represented in an easy and unambiguous way in the form of business models. REAlist uses the Resource-Event-Agent (REA) ontology as business modeling language, since it was initially proposed to support IT-system implementations and is related to data modeling. REA allows the specification of events that have happened or are happening in the near future, resources affected by the events, and agents participating in them. Furthermore policies and commitments can be defined, which are both important concepts for ERP-systems. The underlying database of the REAlist project (REA-DB) is based on REA. Its data structure is generic, meaning that changed business needs (defined with REA concepts) can be saved without changing it. Instead of using the classic class-diagram-like representation of REA, a domain specific language (REA-DSL) is used to simplify the creation of REA business models.

The aim of this thesis is to undertake the first steps of the REAlist project and create a mapping from REA-DSL business models to the generic REA-DB. Furthermore user interfaces are (semi-)automatically generated based on the saved models during runtime to reduce the effort that is needed during the customization tasks in existing ERP-systems.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Gürth_paper.pdf) and [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Gürth_poster.pdf)