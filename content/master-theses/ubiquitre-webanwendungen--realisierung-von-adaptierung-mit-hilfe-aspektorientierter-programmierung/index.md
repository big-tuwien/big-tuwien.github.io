---
authors:
- Petra Brosch
categories: []
date: '2020-05-08 14:38:41+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Ubiquitäre Web-Anwendungen - Realisierung von Adaptierung mit Hilfe aspektorientierter
  Programmierung
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in October 2006.

Ubiquitäre Web-Anwendungen haben das anytime/anywhere/anymedia Paradigma zugrunde liegen, und sollen dem Anwender, egal wann, wo und mit welchem Gerät er diese nutzt, einen individuell abgestimmten und auf die Rahmenbedingungen des Benutzers angepassten Inhalt bieten.

Im Rahmen einer Kooperation von drei Magisterarbeiten \[Brosch, Mayer, Weissensteiner\] wurde ein ubiquitäres Tourismusinformationssystem entwickelt. Das Ziel dieses umfangreichen Projekts war die Konzeption, Modellierung und Implementierung einer Web-Anwendung mit Customizationunterstützung, dh. einer Web-Anwendungen die aufgrund mehrerer Kontextfaktoren wie Benutzer, Zeit, Ort, Gerät, etc., mit der Adaptierung ihrer Dienste reagiert. Die Implementierung der Customizationfunktionalität ist allerdings komplex, da sie an vielen Stellen der Web-Anwendung Berücksichtigung finden muss und sich quer durch den Code des Systems zieht. Separation of Concerns ist daher im Sinne der Wartbarkeit, Erweiterbarkeit, Änderbarkeit, etc. eines Systems anzustreben.

Der Fokus dieser Arbeit liegt auf Aspektorientierung in der Entwicklung von ubiquitären Web-Anwendungen. Die aspektorientierte Programmierung unterstützt die Modularisierung von so genannten Crosscutting Concerns mit Hilfe eines neuen Konzepts, dem Aspekt. Diese Crosscutting Concerns lassen sich mit herkömmlichen Modularisierungsmethoden, die beispielsweise die objektorientierte Programmierung bietet, nicht kapseln, sondern sind über viele Komponenten eines Programms hinweg verteilt. Typische Beispiele für Crosscutting Concerns sind so genannte System-level Concerns wie Logging, Authentifizierung und Fehlerbehandlung. Die Kernfunktionalität eines Systems, so genannte Core Concerns, lassen sich üblicherweise in Klassen der Geschäftslogik kapseln, nicht so die Customizationfunktionalität. Daher demonstrieren wir anhand eines ubiquitären Tourismusinformationssystems den Nutzen und Beitrag von Aspektorientierung zur Behandlung von Separation of Concerns im Allemeinen und insbesondere für die Trennung des Customization Concerns.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Brosch_paper.pdf) and [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Brosch_poster.pdf)

*Advised by {{% mention "andrea-schauerhuber" %}}, {{% mention "gertrude-kappel" %}}*