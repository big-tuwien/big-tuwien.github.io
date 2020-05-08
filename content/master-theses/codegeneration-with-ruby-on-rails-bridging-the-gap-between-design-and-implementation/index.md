---
authors:
- Alexander Dick
categories: []
date: '2020-05-08 15:28:04+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Codegeneration with Ruby on Rails – Bridging the gap between Design and Implementation
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in October 2006.

Durch die Veränderung des World Wide Web von einem statischen Informationsmedium hin zu einem dynamischen Anwendungsmedium ist der Bedarf an Webanwendungen, die für die Bereitstellung von Diensten über das Web verantwortlich sind, so hoch wie nie. Es haben sich bereits sehr viele Technologien etabliert, mit Hilfe derer es möglich ist, Webanwendungen zu entwickeln. Die Anforderungen an solche Webanwendungen sind sehr vielfältig und mit einer oft kürzeren Entwicklungszeit, die für die Erzeugung der Anwendung zur Verfügung steht, geht eine meist höhere Komplexität der benötigten Funktionalität einher.

Um es den Entwicklern zu ermöglichen, sich mit dem eigentlichen Problem auseinander zu setzen und nicht für jede Webanwendung das Rad neu erfinden zu müssen, werden für die verschiedenen Technologien Frameworks geschaffen, die den Programmierer mit Hilfe integrierter Funktionalitäten bei der Implementierung unterstützen sollen.

Eines dieser Frameworks, das sich erst seit kurzer Zeit im Web etabliert, ist Ruby on Rails. Es bietet Funktionalitäten, die es dem Entwickler ermöglichen rasch einen ersten, funktionstüchtigen Prototyp einer Webanwendung zu generieren, mit Hilfe dessen sofort Feedback vom Benutzer eingeholt werden kann. Wie es bei vielen Anwendungen im Web der Fall ist, basieren auch die Applikationen, die mit Ruby on Rails erstellt werden auf einem relationalen Datenbanksystem. Der Prototyp, der mit Hilfe eines in Rails integrierten Codegenerators erzeugt wird, bietet jedoch nur eingeschränkte Funktionalität und es wäre wünschenswert einerseits diese zu erweitern und andererseits die Anwendung ausgehend von einem Modell, das die Datenbank beschreibt, generieren zu können.

Diese Arbeit versucht in einem ersten Schritt den von Ruby on Rails bereitgestellten Scaffold-Generator so zu erweitern, dass der Prototyp auch Validierungsfunktionalität beherrscht. Dies geschieht mit Hilfe zweier zusätzlicher Datenbanktabellen, die Regeln für die Validierung bereitstellen sollen. Weiters soll die Abbildung von Beziehungen zwischen Datenbanktabellen automatisch in die Modellklassen der Webanwendung eingebunden werden.

Im zweiten Schritt wird ein grafischer Editor erstellt, der für die Erstellung von logischen Datenbankmodellen herangezogen werden kann.

Schließlich soll am Ende ein Framework entstehen, das zuerst zur Modellierung von ER-Diagrammen dient, danach aus dem Modell über einen Zwischenschritt der Codegeneration die Struktur der Datenbank erstellt und zum Abschluss mit Hilfe des erweiterten Ruby-Generators den Prototyp einer datenintensiven Webanwendung erstellt. Aufgrund der Kombination von Modellierung und dem Einsatz von Ruby on Rails wird dieses Framework Models on Rails genannt.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Dick_paper.pdf) and [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Dick_poster.pdf)

*Advised by {{% mention "manuel-wimmer" %}}, {{% mention "gertrude-kappel" %}}*