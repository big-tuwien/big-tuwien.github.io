---
authors:
- Thomas Franz
- Sabine Wolny
categories: []
date: '2020-05-08 15:44:47+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Automatisiertes White-box Testen von Regel-basierten Modelltransformationen
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in September 2013.

Seit mehreren Jahren ist die modellgetriebene Softwareentwicklung (englisch: Model Driven Engineering (MDE) beziehungsweise Model Driven Software Development (MDSD)) auf dem Vormarsch und Softwaremodelle werden nicht mehr nur für Entwurfszwecke genutzt, sondern sind ein Hauptelement im Software Engineering Prozess geworden. Modellierungssprachen wurden entwickelt um Modelle darzustellen, die eine Basis für die weitere Entwicklung bilden. Die bekannteste Modellierungssprache ist Unified Modeling Language (UML), ein Standard der Object Management Group (OMG). In diesem Zusammenhang stehen auch Ecore Metamodelle, welche der Hauptbestandteil von Eclipse Modeling Framework (EMF) sind und als vereinfachte UML Klassendiagramme gesehen werden können. Neben den Modellierungssprachen spielen in der modellgetriebenen Softwareentwicklung auch Modelltransformationen eine entscheidende Rolle. Das Ziel einer Modelltransformation ist ein bestimmtes Quellmodell in ein gewünschtes Zielmodell zu transformieren. Eine der bekanntesten regelbasierten Modelltransformationssprachen ist die Atlas Transformation Language (ATL). Oftmals schlagen Transformationen fehl und die Fehlererkennung ist mühsam und langwierig, da diese in der Transformation selbst oder in den Metamodellen liegen können. Ziel dieser Arbeit ist es einen automatisierten Ablauf zu finden, der regelbasierte Transformationen testen kann. Dabei soll ein Tool in Java entwickelt werden, welches auf der Metamodellierungssprache Ecore und regelbasierten Modelltransformationen in ATL aufbaut. Hierbei beschäftigt sich die Diplomarbeit mit mehreren Fragen. Ist es möglich einen White Box Test Ansatz für ATL Transformationen zu finden? Wie können Modelle(Testinstanzen) aus einem Metamodell automatisch generiert werden? Wie hoch ist die Fehlererkennungsrate? Welche Art von Fehlern können bei den Transformationen festgestellt werden? In dieser Arbeit werden zuerst die nötigen Grundlagen wie zum Beispiel Answer Set Programming (ASP) und Testen im Allgemeinen erläutert. Anschließend wird auf die konkrete Implementierung eines möglichen Ansatzes eingegangen. Abschließend wird die Evaluierung des entwickelten Tools anhand der vorhandenen Übungsaufgaben zum Thema Modelltransformationen aus der Lehrveranstaltung “Model Engineering” der Technischen Universität Wien der Jahre 2008 bis 2012 präsentiert und ein Ausblick für weitere Möglichkeiten gegeben.

&nbsp;

*Advised by {{% mention "gertrude-kappel" %}}*