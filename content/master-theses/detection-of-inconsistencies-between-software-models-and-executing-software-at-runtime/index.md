---
advisors:
- manuel-wimmer
authors:
- Daniel Lehner
categories: []
date: '2020-05-11 21:33:09+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Ongoing
title: Detection of inconsistencies between software models and executing software
  at runtime
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

Emerging technologies such as self-adaptive software, Internet of Things (IoT) and Distributed Systems (DS) as well as an increasing scalability of software systems complicate predicting whether a software system will behave as expected based on verification of its static properties or not. Additionally, software providers tend to reduce their release cycles due to increasing volatility of requirements in an agile software development environment. This makes extensive testing of software more and more difficult. Verification is usually based merely on automated tests that mostly neglect the runtime behavior of a system. This might lead to impactful problems in various areas. For instance, imagine driving an “autonomous car”. This car is connected to various external systems, or even other cars, that might determine decisions it takes while driving to defined locations. It is relevant for occupants whether the system behaves as expected. Or imagine living in a so-called “Smart Home”. It is important that the connected distributed devices in the system behave only as intended by the owner. In addition, this should be verifiable.  
 In my master thesis, I want to focus on creating a framework that automates the verification of runtime behavior of a software system. Therefore, it compares UML sequence diagrams created from runtime log traces with existing diagrams that represent the current state of requirements of the system. Additionally, I want to create generic methods for specific tasks in implementing such a framework (like loading models or classifying inconsistencies) that can be reused to facilitate further research in this area.