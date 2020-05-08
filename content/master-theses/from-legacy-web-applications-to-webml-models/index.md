---
authors:
- Max Rieder
categories: []
date: '2020-05-08 15:18:37+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: FROM LEGACY WEB APPLICATIONS TO WEBML MODELS
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in December 2009.

In the last decade the adoption of web applications instead of desktop applications has grown rapidly. Also the patterns and technologies for developing and running web applications have changed a lot over time. The World Wide Web has evolved from a collection of linked static documents to a space of countless dynamic, data centric applications. One of the oldest and most popular languages for developing dynamic web applications is PHP. Although nowadays there are proved techniques for developing web applications in PHP, many older PHP web applications are written without the notion of applying well-defined design patterns. Those web applications are hard to understand, maintain, extend as well as hard to migrate to new web platforms. Nowadays many web applications are developed using Model Driven Engineering (MDE) techniques where software systems are described as models and code artifacts are generated out of these models. But often the requirement is not to develop a completely new web application but to capture the functionality of an existing legacy application. As it usually takes a lot of time for humans to understand the source code, it can be helpful to have a tool that analyzes the source artifacts and transforms them into a model on a higher level of abstraction. This process is called reverse engineering. The requirements for such a tool to work is the existence of well-known patterns in the source code, which is typically found in Model-View-Controller (MVC) web applications. In this thesis a reverse engineering process from a legacy PHP web shop application into a model of the Web Modeling Language (WebML), based on static code analysis, is presented. First of all the requirements for the source code are analyzed in order to apply an automatic reverse engineering process on it. The source application is refactored to fulfill these requirements, which leads to a MVC version of the example application. The refactored application is the source for the next step, a code to model transformation into an intermediate model of the MVC web application. The last step is a model to model transformation from the the MVC model into a WebML model. The result is aWebML model that shows the most important structural and behavioral aspects of the example application. The benefit of such a model is that that it provides a realistic documentation of the current state of the application. Whenever the application changes, the process can be repeated so the documentation never gets outdated. It helps humans to understand the connections between different parts of the application and can be used to support refactoring activities or the migration to another platform.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Rieder_paper.pdf) and [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Rieder_poster.pdf)

*Advised by {{% mention "manuel-wimmer" %}}, {{% mention "gertrude-kappel" %}}*