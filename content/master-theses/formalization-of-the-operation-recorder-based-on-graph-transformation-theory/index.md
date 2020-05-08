---
authors:
- Sebastian Gabmeyer
categories: []
date: '2020-05-08 14:38:43+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Formalization of the Operation Recorder based on Graph Transformation Theory
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in April 2011.

Software engineering has come a long way in its short history. With the recent advent of modeldriven development, which places models at the center of all development efforts, some of the existing deficiencies of traditional, code-centric software development approaches have been addressed. However, at the same time new problems arose, which require, for example, techniques to describe, control and verify the evolution of models. Drawing from past experiences and findings in the field of code-centric software evolution is only partly feasible due to the inherent graph-based nature of models, which renders the adoption and porting of previously developed solutions for text-based software development impractical.

The graph-based nature of models suggests the application of graph transformation-theoretic concepts to models, in order to formally describe their manipulation by means of graph-rewriting rules. Though the concepts and techniques provided by the theory of graph transformation may seem intuitive, the specification of accurate rewriting rules is a non-trivial and time-consuming task, which requires adequate tool support and thorough knowledge of the underlying theory. Unfortunately, due to the heterogeneity of the employed approaches, a tool’s capability to specify graph rewriting rules and the degree of assistance offered for this task is hard to determine without prior investigation. Thus, a survey of existing tools was conducted, which revealed the Operation Recorder as a suitable tooling environment. In contrast to all other surveyed tools, it offers a by-demonstration environment, which allows to showcase the intended transformation instead of requiring its manual construction by means of dedicated transformation languages.

The Operation Recorder, however, lacks a concise, formal basis which prevents the verification of its ransformations. Therefore, a framework to describe attributed graphs with inheritance, composition and multiplicities is presented with the aim to embed the Operation Recorder into this framework. For this purpose, a conceptual alignment is pursued which demonstrates the equivalence and interchangeability of the concepts provided by the Operation Recorder and those provided by the theory of graph transformation.

Abstract and paper may be found in our <a class="external" href="http://publik.tuwien.ac.at/showentry.php?ID=196648&amp;lang=2">publication database</a>.

 Download the [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Gabmeyer_poster.pdf)

*Advised by {{% mention "martina-seidl" %}}, {{% mention "petra-kaufmann" %}}, {{% mention "gertrude-kappel" %}}*