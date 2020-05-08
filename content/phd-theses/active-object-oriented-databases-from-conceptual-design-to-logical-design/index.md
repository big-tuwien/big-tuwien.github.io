---
authors:
- Werner Obermair
categories: []
date: '2020-05-08 15:45:04+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: 'Active Object-Oriented Databases: From Conceptual Design to Logical Design'
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in February 1998.

The design of active object-oriented databases includes modeling the structure of objects, their passive behavior in the form of operations that can be performed on them, and their active behavior in the form of business rules. Business rules are statements about business policies and can be formulated according to the event-condition-action structure of rules provided by active database systems, which allow to react to predefined situations by performing an operation if a certain condition is satisfied when the event occurs.

An approach that has been followed successfully in conventional database design is to perform database design in two phases: In the first phase, the conceptual design, a high-level graphical representation of the database schema is developed. In the second phase, the logical design, the developed schema is mapped to the data model of the system used for the implementation. We adopt this approach for the design of active object-oriented databases.

We introduce Active Object/Behavior Diagrams for the conceptual design of active object-oriented databases. Active Object/Behavior Diagrams seamlessly extend Object/Behavior Diagrams, an existing high-level graphical language for modeling the structure and the passive behavior of objects, with concepts for modeling business rules. Modeling business rules at the conceptual level requires different concepts than currently provided by active object-oriented database systems and by recent approaches to active object-oriented database design. Active Object/Behavior Diagrams introduce a graphical rule and event language the meets the identified requirements.

During logical design, a schema developed with Active Object/Behavior Diagrams is mapped to a logical schema of an existing active object-oriented database system. We present such a mapping for TriGS, a prototype of an active object-oriented database system built on top of the commercial object-oriented database system GemStone (GemStone Systems, Inc.). The mapping decomposes the high-level constructs of Active Object/Behavior Diagrams into lower-level constructs of TriGS. The presented mapping covers all three dimensions of a schema specified with Active Object/Behavior Diagrams: object structure, passive object behavior, and active object behavior.

&nbsp;

*Advised by {{% mention "gertrude-kappel" %}}*