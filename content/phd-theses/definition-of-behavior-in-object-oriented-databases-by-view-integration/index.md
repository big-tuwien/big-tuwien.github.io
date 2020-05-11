---
advisors:
- gertrude-kappel
authors:
- Günter Preuner
categories: []
date: '2020-05-11 21:33:31+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Definition of Behavior in Object-Oriented Databases by View Integration
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in September 1998.

Databases in large organizations are usually designed by a group of people including potential future users of the database who know the application domain from everyday business. The design of databases by view integration means that several users or groups of users define their views on the proposed database. These views are collected and integrated to one conceptual database schema.

We treat view integration in the context of modeling business processes and workflows and use the object-oriented data model Object/Behavior Diagrams to define the structure and behavior of business objects. In this work, we will focus on the definition and integration of views of the behavior of objects. Behavior of business objects is defined based on a two-schema architecture: Business processes define the overall behavior of business objects according to external business rules, which mainly reflect long-term business rules due to natural facts or law; workflows represent the current processing of business objects in an organization according to internal business rules.

Users define their views as they perceive processing of business objects in everyday business, thereby modeling workflows. Further, views of different users comprise different information: (1) Views model behavior of different entities of the real world; (2) views define processes at different levels of detail or omit parts of the processes; (3) views contain comparable information that is defined using different modeling concepts; (4) views define specifications of activities by providing an interface or refer to activities without defining an interface.

The goal of view integration is to define the complete set of object types and business processes in the conceptual database schema. Thus, information relevant for the business processes is extracted from the workflows, the object types of the integrated schema are determined, and a business process as well as the activity specifications are defined for each object type. The goal of view integration is to define object types with business processes in a way that the processing of objects according to a business process in the conceptual schema can be observed as a correct processing in each view if information that is not defined in the view is ignored.

&nbsp;