---
authors:
- Gerald Müller
- Abraham Müller
categories: []
date: '2020-05-08 15:18:35+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: 'Model Transformation By-Example: An Eclipse based Framework'
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in June 2008.

Viele momentan existierenden Ansätze sowie Sprachen zur Modelltransformation sind metamodel-basiert, sie setzen detaillierte Kenntnisse der Metamodellebene und deren Syntax voraus. Meist wird die Transformation durch ein vollständiges Regelwerk auf der Metaebene bewerkstelligt. Einen neuen benutzerfreundlichen Ansatz dafür beschreibt die Model Transformation by-Example (MTBE), hierbei wird von einem leeren Regelwerk ausgegangen, bei dem der Benutzer auf Instanzebene grafisch die gewünschten Mappings defineren kann, aus denen dann automatisch Regeln generiert werden. Dies hat zum einen den Vorteil, dass auch Modelle transformiert werden können für welche noch keine Regeln existieren, zum anderen, dass der Benutzer individuelle Regeln erstellen kann ohne mit dem Metamodell oder der Transformationssprache vertraut zu sein. In dieser Arbeit wird versucht, ein Framework für MTBE auf Basis des Graphical Modelling Framework (GMF) zu implementieren. In unserer Implementation wird MTBE in ein Eclipse Plugin eingebettet, die Mappings können mit Hilfe eines automatisch, passend generiertem GMF-Editor gezeichnet werden. Daraus wird mittels eines Analyzers ein Weaving Model beziehungsweise der ATL Regelsatz generiert. In unserer Arbeit werden die dazu nötigen Grundlagen wie beispielsweise das Eclipse Modelling Framework oder die Atlas Transformation Language erläutert, anschließend wird die konkrete Implementation des Frameworks vorgestellt.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Müller_Müller_paper.pdf) and [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Müller_Müller_poster.pdf)

*Advised by {{% mention "michael-strommer" %}}, {{% mention "gertrude-kappel" %}}*