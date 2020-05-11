---
advisors:
- andrea-schauerhuber
- gertrude-kappel
authors:
- Cornelia Tomasek
categories: []
date: '2020-05-11 21:33:23+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Integration von Crosscutting Concerns in aspectWebML
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in January 2008.

Ubiquitäre Web-Anwendungen werden nach dem anytime/anywhere/anymedia Paradigma individuell auf den Benutzungskontext, wie zum Beispiel Zeit, Ort oder Endgerät angepasst. Die Durchführung solcher Customizations ist oft komplex, da sich eine Änderung meist nicht nur auf einen bestimmten Teil der Web-Anwendung bezieht, sondern eine Vielzahl von Stellen betrifft, die in den verschiedenen Ebenen der Web-Anwendung, Content, Hypertext und Präsentation liegen. Im Bereich des Model Driven Engineering ziehen die meisten Web-Modellierungssprachen diese Eigenschaft von Customizations nicht gesondert in Betracht. Änderungen werden, so wie herkömmliche Anpassungen des Models, an mehreren Stellen direkt im Kern-Model vorgenommen. Diese Vorgehensweise führt allerdings bezüglich Wartbarkeit und Erweiterbarkeit zu einer erhöhten Komplexität und damit zu einem ineffizienten Entwicklungsprozess. In aspectWebML, einer Erweiterung der Web-Modellierungssprache WebML, werden Customizations dagegen als so genannte Crosscutting Concerns im Sinne der Aspektorientierung betrachtet und mit Hilfe spezieller aspektorientierter Konzepte behandelt. Diese ermöglichen eine klare Trennung bei der Modellierung von Kernfunktionalität und Crosscutting Concerns, wodurch eine Reduzierung der Komplexität der Modelle, eine Verbesserung der Wartbarkeit sowie der Wiederverwendbarkeit einzelner Customizations erreicht wird. Als Teil des Modellierungsprozesses muss dieser klaren Trennung von Kernfunktionalität und Crosscutting Concerns aber auch ein geeigneter Mechanismus gegenübergestellt werden, der die einzelnen Teile wieder zu einem Gesamtmodel, dem Ergebnis der Modellierung, integriert.

Das Ziel dieser Arbeit ist daher die Implementierung eines Algorithmus zur Integration von Crosscutting Concerns in aspectWebML auf Basis der bestehenden aspektorientierten Konzepte. Dabei sollen die Anforderungen an solch eine Integration analysiert werden und eine geeignete Technologie gewählt werden, um die 13 verschiedenen Möglichkeiten zur Modellierung von Customization-Szenarien in aspectWebML umsetzen zu können. Der Algorithmus soll in ein vorhandenes Modellierungswerkzeug integriert werden, das mittels EMF (Eclipse Modeling Framework) erzeugt und um verschiedene Funktionalitäten zur Unterstützung des Modellierers erweitert wurde, sowie anhand verschiedener Customization Szenarien überprüft werden.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Tomasek_paper.pdf) and [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Tomasek_poster.pdf)