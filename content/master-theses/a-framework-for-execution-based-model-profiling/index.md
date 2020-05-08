---
authors:
- Polina Patsuk-Bösch
categories: []
date: '2020-05-08 15:28:02+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Ongoing
title: A Framework for Execution-based Model Profiling
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

In Model-Driven Engineering (MDE) models are used throughout the software development process in prescriptive ways. Such prescriptive models are important during the implementation phase of software and systems. In addition, there are descriptive models generated from runtime data offering valuable information in one of the later phases of a system’s life cycle. Unfortunately, descriptive models are only marginally explored in the field of MDE. Current MDE approaches mostly neglect the possibility to combine prescriptive and descriptive models in a unifying framework to link downstream and upstream information. To bridge this gap, we propose such a framework by loosely couple MDE approaches with process mining (PM) techniques. This framework enables us to support execution-based model profiling as continuous monitoring process over the entire life cycle of a system. In the course of this thesis, we provide an evaluation case study in order to demonstrate the feasibility and benefits of the introduced approach. For this purpose we implement a prototype of our framework, which registers logs from a running traffic light system. This system is modeled both, in a basic and extended object-oriented way. The prototype transforms the registered logs of systems into XES-format in order to apply established PM algorithms (e.g., inductive miner). Further, we evaluate different PM algorithms (e.g., α-algorithm, inductive miner) to determine the most efficient one for our approach.

*Advised by {{% mention "manuel-wimmer" %}}, {{% mention "alexandra-mazak" %}}*