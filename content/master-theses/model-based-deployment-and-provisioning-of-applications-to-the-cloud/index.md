---
advisors:
- alexander-bergmayr
- manuel-wimmer
authors:
- David Madner
categories: []
date: '2020-05-11 21:33:17+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Model-based Deployment and Provisioning of Applications to the Cloud
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in December 2013.

Cloud computing had and still has a major impact on how applications are made accessible for the users. Due to the advantages cloud computing has, there is a demand to migrate applications to the cloud. Unfortunately there does not exist general guidelines how to define the required application execution environments and deployment requirements so that they can be interpreted by any arbitrary cloud provider.

In the last years, cloud providers came up with approaches to be able to describe cloud resources in form of an interpretable template. Just recently, in November 2013, OASIS published the open standard TOSCA, which aims to unite existing proprietary approaches and standardise them. Approaches following a declarative way of describing orchestrated cloud resources are quite recent and are extended frequently, as it is a promising possibility of illustrating complex dependencies and limitations of computing resources in a way that can be read by human beings as well.

This thesis firstly discusses model driven engineering and cloud computing separately and afterwards, how they can be combined. The main aim is to create a model that contains enough information about dependencies, limitations and application specific requirements, which can support the migration of the application to the cloud.

Furthermore, the master’s thesis proposes a process, which is subdivided into two parts: Deployment and Provisioning. The first step is about creating UML models and refining them with UML extensions (classifiers, profiles and stereotypes), which consists out of cloud computing specific attributes. The second step converts the model into a template, by means of applying model to text transformations, in order to be interpretable and executable by cloud providers.

Existing solutions only address partial aspects of the whole problem, focusing on other objectives. One of the main goal of this thesis is the creation of a unified and model-based solution, whose processes and tools support the application modeler and make a (semi-)automatic execution of the deployment and provisioning of an application in the cloud possible.

&nbsp;