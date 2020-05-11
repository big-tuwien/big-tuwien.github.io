---
advisors:
- gerhard-kramler
- gertrude-kappel
authors:
- Arnold Karner
categories: []
date: '2020-05-11 21:33:15+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Codegenerierung mit AndroMDA
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in October 2006.

Mit der Model Driven Architecture (kurz: MDA) gibt es einen neuen Standard zur generativen Softwareentwicklung. Dieser wurde von der Object Management Group im Juni 2003 spezifiziert. Ziel der MDA ist es, technologienunabhängige Spezifikationen zu erstellen, die für automatische Codegenerierung auf unterschiedlichen Plattformen wie .NET, J2EE, oder CORBA genutzt werden können.

Mit dem Einsatz von MDA liegt der Fokus hauptsächlich auf der Modellebene, die eigentliche Programmierung rückt zusehends in den Hintergrund. Der Idealfall wäre eine auf unterschiedlichen Plattformen völlig automatisierte sowie vollständige Codegenerierung aus den UML Modellen. Da dies aber noch nicht der Fall ist, müssen Software Entwickler bis dato auf 2 unterschiedlichen Abstraktions- und Technologieebenen, der Modellebene und der Codeebene, arbeiten.

Bis dato implementieren schon eine geraume Anzahl von Tools die MDA Spezifikation (AndroMDA, ArcStyler, Rational Software Architect etc.). Das in dieser Arbeit untersuchte AndroMDA ist ein Open Source Framework und wurde im März 2003 vorgestellt. Es benutzt zur Codetransformation aus UML-Modellen verschiedene, sogenannte Cartridges1. Mit diesen Cartridges verarbeitet AndroMDA Metamodell-Elemente die durch Stereotypen und Schlüsselwörtern, wie z.B. «Entity» oder «Service» gekennzeichnet werden und generiert daraus Codefragmente. AndroMDA unterstützt derzeit primär die Zielsprachen Java und C\#/.NET. Die Codegenerierung wird über Templates gesteuert, so dass jede erdenklich Zielsprache (HTML, PHP etc.) damit realisiert werden kann.

Ziel dieser Magisterarbeit ist es, das MDA Framework „AndroMDA“ anhand einer Beispielanwendung (Onlinebuchhandlung) zu evaluieren. Hierbei soll die Funktionsweise der einzelnen Komponenten, unterstützte Technologien sowie Stärken und Schwächen des Frameworks bezüglich Codegenerierung ermittelt werden. Aus diesen Ergebnissen soll im weiteren Verlauf der Arbeit die Codegenerierungsfunktionalität hinsichtlich möglichst vollständiger Codegenerierung optimiert werden.

Als Grundlage dieser Untersuchungen, dient das Referenzbeispiel „Onlinebuchhandlung“. Zuerst soll die Anwendung der Onlinebücherei als UML Modell abgebildet und modelliert werden. Im weiteren Verlauf muss das UML Modell an die Erfordernisse AndroMDA’s so angepasst werden (Stereotypen), dass es als Input für die Codegenerierung (Cartridges) dienen kann. Anschließend werden die jeweiligen Codefragmente generiert. Danach soll die Codegenerierungsfunktionalität analysiert und Verbesserungspotential davon abgeleitet werden. Nach diesem Schritt werden ausgewählte Verbesserungsmöglichkeiten bezüglich der Vollständigkeit der Codegenerierung (z.B. mittels Entwicklung eigener oder erweiterte Cartridges) anhand der gleichen Referenzanwendung entwickelt und evaluiert.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Karner_paper.pdf) and [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Karner_poster.pdf)