---
authors:
- Andrea Schauerhuber
categories: []
date: '2020-05-08 14:38:50+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Entwicklung eines webbasierten Institutsinformationssystems - Separation of
  Concerns und seine Umsetzung in LAMP
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in October 2004.

Im Rahmen einer Kooperation dreier laufender Diplomarbeiten (Alexander Heumayer, Nenad Jovanovic, Andrea Schauerhuber) wurde mit Hilfe der Open-Source Web- Development-Plattform LAMP (der Kombination aus dem Betriebssystem Linux, dem Webserver Apache, dem Datenbank-Managementsystem MySQL und der Programmiersprache PHP) ein für die Business Informatics Group (Institut für Softwaretechnik und Interaktive Systeme, Technische Universität Wien) maßgeschneidertes Web-Informationssystem entwickelt. Die Web-Anwendung bietet unterschiedlichen Benutzergruppen, darunter Studierenden und Mitarbeitern des Instituts, verschiedenste Dienste an.

Der Schwerpunkt der vorliegenden Diplomarbeit ist die Entwicklung eines Architektur- Frameworks für LAMP, das den Anforderungen des Separation of Concerns von Web-Informationssystemen gerecht wird. Die Schwäche der traditionellen Entwicklung unter LAMP liegt in der Vermischung von Inhalten, Anwendungslogik und Präsentation. Zum einen erlaubt HTML keinen Rückschluss auf die Semantik der Inhalte von HTML-Tags, wodurch Inhalte und Präsentation nicht voneinander getrennt werden können. Zum anderen sorgt hinzugefügter PHP-Code, der die Anwendungslogik einbringen soll, für zusätzliche Komplexität. Die Hauptanforderung an die zu entwickelnde Architektur war es daher, diese Schwächen zu beseitigen und im Sinne des Diplomarbeitstitels dem Separation of Concerns-Paradigma zu folgen. Die in der Diplomarbeit entwickelte Architektur basiert auf dem XAO Framework (http://xaophp.sourceforge.net), erweitert um die Realisierung des Model View Controller Patterns. Diese Architektur stellt auch die Grundlage für das im praktischen Teil entwickelte Institutsinformationssystem dar.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Schauerhuber_paper.pdf)

*Advised by {{% mention "gertrude-kappel" %}}*