---
authors:
- Benedikt Weismann
categories: []
date: '2020-05-08 15:18:41+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Architekturzentrierte Modellgetriebene Softwareentwicklung - Fallbeispiel und
  Evaluierung
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in September 2006.

In den vergangenen zwei Jahrzehnten hat Software eine immer stärkere Bedeutung in zahlreichen Geschäftsprozessen und alltäglichen Informationsflüssen erlangt. Sie stellt gewissermaßen das Fundament dieser Abläufe dar. Software ist zu einem kritischen Bestandteil vieler Unternehmen und Lebensbereiche geworden. Analog zu dieser Bedeutunksteigerung stehen die Entwicklungsmethoden mehr und mehr im Spannungsfeld von hoher Qualität des Endprodukts und niedrigen Entwicklungskosten bzw. kurzen -zyklen. In der Realität können viele Projekte diesen Ansprüchen nicht gerecht werden. Um den Softwareschaffenden neue Werkzeuge zu bieten, die es ermöglichen diese gegensätzlichen Ziele zu vereinbaren, gibt es seit geraumer Zeit, die Bestrebung Code automatisch aus einem Modell der zu entwickelnden Applikation zu generieren.

Einer dieser Ansätze ist die Modellgetriebene Software Entwicklung (eng: Model Driven Software Development, kurz MDSD). Bei MDSD wird basierend auf einem in den meisten Fällen graphischen Modell durch Transformationen lauffähiger Sourcecode erzeugt. Stahl und Völter beschreiben in ihrem Buch „Modellgetriebene Software Entwicklung“ \[1\] einen pragmatischen Ansatz um mit Hilfe von MDSD und bereits heute verfügbaren Techniken den Infrastrukturcode einer Applikation bzw. einer ganzen Software-Systemfamilie zu generieren. Diesen Ansatz bezeichnen sie als architekturzentrierte-MDSD (AC-MDSD). Es wird dabei versucht den Infrastrukturcode einer definierten Softwaresystemfamilie möglichst vollständig zu generieren. Eine Softwaresystemfamilie ist die Summe aller Applikationen die auf derselben Architektur und technologischen Plattform beruhen.

Die Codegenerierung bei AC-MDSD stützt sich auf zwei Säulen. Zum einen werden die verwendeten Modelle mittels einer so genannten Domain Specific Language (DSL) formalisiert. Die DSL spiegelt mit ihren Ausdrucksmitteln den Problemraum der jeweiligen Domäne wieder. Die Konzepte der DSL werden durch ein Metamodell der Domäne abgebildet. Zum anderen erleichtert der Einsatz eines Frameworks und wieder verwendbarer Komponenten die Erzeugung des Sourcecodes, da der „Weg“ zwischen Generat und Modell verkürzt wird.

Im Rahmen dieser Diplomarbeit wird ausgehend von den in \[1\] beschriebenen theoretischen Konzepten und dem von den Autoren des Buches mitentwickelten Codegenerator Toolkit openArchitectureWare (oAW) \[2\], die konkrete Vorgehensweise bei der Softwareerstellung mittels AC-MDSD an Hand eines praktischen Beispiels aus dem Bereich „Softwareinfrastruktur für E-Business-Anwendungen“ veranschaulicht. Die Umsetzung erfolgt mit Hilfe von Technologien aus dem J2EE Bereich wie JSPs, Servlets, Enterprise JavaBeans und dem Webframework Struts. Fachlich handelt es sich dabei um eine Online-Buchhandlung. Im Rahmen der Durchführung soll auch die Erstellung eines GEF-Editors für die DSL mit Hilfe von oAW veranschaulicht werden. Neben diesen praktischen Aspekten der Arbeit werden die für das Verständnis nötigen theoretischen Konzepte dargelegt, und eine Abgrenzung zu verwandten Methoden wie MDA durchgeführt. Abschließend wird eine kritische Evaluierung hinsichtlich der Praxistauglichkeit des vorgestellten Ansatzes vorgenommen. Dabei werden sowohl dessen Stärken als auch Schwächen gegenübergestellt.

Quellenverzeichnis

\[1\] Markus Völter, Thomas Stahl; Modellgetriebene Softwareentwicklung. dpunkt.verlag, 1. Auflage 2005 \[2\] www.openarchitectureware.org

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Weismann_paper.pdf) and [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Weismann_poster.pdf)

*Advised by {{% mention "gerhard-kramler" %}}, {{% mention "gertrude-kappel" %}}*