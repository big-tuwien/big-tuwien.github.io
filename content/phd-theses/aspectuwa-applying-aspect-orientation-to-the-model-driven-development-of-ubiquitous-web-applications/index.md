---
advisors:
- gertrude-kappel
authors:
- Andrea Schauerhuber
categories: []
date: '2020-05-11 21:33:32+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: aspectUWA - Applying Aspect-Orientation to the Model-Driven Development of
  Ubiquitous Web Applications
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in October 2007.

Ubiquitous web applications (UWA) are a new type of web applications which are accessed in various contexts, i.e., through different devices, by users with various interests, at anytime from anyplace around the globe. In this respect, customization functionality exploits information on this context of use in order to adapt the application’s services accordingly. In web application development, customization is considered a new dimension which increases complexity by ”crosscutting” the content, hypertext, and presentation levels of a web application. Hence, from a software engineering point of view, a systematic development of UWAs on the basis of models is crucial. In model-driven engineering (MDE), models are employed ”as programs” to (semi-) automatically generate applications, which results in more efficient development processes as well as better maintainability and evolution of software. Customization functionality, however, is typically intermingled with the core functionality in a web application model, having a negative effect on understandability, reuse, maintenance and evolution. The aspect-orientation paradigm provides a new way of modularizing crosscutting concerns such as customization within so-called aspects, as well as the necessary means for composing the previously separated concerns in order to obtain the complete application model. There are already some web modeling approaches dealing with the ubiquitous nature of web applications, amongst them, first proposals to use aspect-orientation. Nevertheless, these approaches suffer from the following problems: First, they don’t consider the crosscutting nature of customization comprehensively, but for the hypertext level, only. Second, just very basic aspect-oriented modeling (AOM) concepts are used, resulting in less powerful mechanisms for separating customization. Third, composition of concerns is not regarded for the modeling level. And fourth, model-driven development of UWAs in the sense of MDE is still limited due to missing metamodel specifications and lack of tool support.

The overall aim of this thesis is the exhaustive use of aspect-orientation as driving paradigm for comprehensively modeling customization aspect separately from all web application levels as well as providing means for composing the aspect with the web application model. Therefore, this thesis proposes the aspectUWA approach, which suggests a generic framework for extending existing web modeling languages with AOM concepts within the realms of MDE. In the context of this thesis, aspectUWA is applied to the web modeling anguageWebML, which doesn’t allow to separately model customization. The major contributions of this thesis are as follows: (i) A Conceptual Reference Model (CRM) for AOM has been developed to form the aforementioned general framework. (ii) A metamodel for WebML has been semi-automatically generated from an existing DTD-based language specification in order to allow for MDE. (iii) The aspectWebML language has been desiged on basis of the CRM and represents WebML’s port to AOM allowing for modeling customization separately as well as for composing the customization aspect with the rest of the web application model. (iv) An initial set of guidelines to be used for modeling customization within aspectWebML is proposed. And (v), the aspectWebML Modeling Environment provides the often missing tool support for modeling crosscutting concerns as well as their composition.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Schauerhuber_A.pdf)