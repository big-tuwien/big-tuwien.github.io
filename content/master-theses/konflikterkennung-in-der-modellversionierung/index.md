---
authors:
- Philip Langer
categories: []
date: '2020-05-08 14:38:46+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Konflikterkennung in der Modellversionierung
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in February 2009.

In den letzten Jahren gewannen Softwaremodelle als zentrale Artefakte der Softwareentwicklung zunächst mit dem CASE-Ansatz (Computer Aided Software Engineering) und später mit dem MDE-Ansatz (Model Driven Engineering) immer mehr an Bedeutung. Sie dienen mittlerweile nicht nur zur Dokumentation und zur Bildung des gemeinsamen Verständnisses sondern auch als Grundlage für die Generierung eines lauffähigen Systems. Der modellgetriebene Ansatz ist in der Softwareentwicklung zu einer etablierten und weit verbreiteten Methode geworden.

An dem Softwareentwicklungsprozess ist in größeren Softwareprojekten üblicherweise eine Vielzahl an EntwicklerInnen beteiligt. Diese verfeinern in einem zumeist iterativen Prozess das zu entwickelnde System und passen es stetig an sich verändernde Anforderungen, Verständnisse und laufend zu treffende Designentscheidungen an. Für eine erfolgreiche Durchführung eines Softwareprojekts ist daher ein effizientes Änderungs- und Konfigurationsmanagement ausschlaggebend und ermöglicht erst die effektive Zusammenarbeit mehrerer EntwicklerInnen. Traditionelle Versionierungssysteme implementieren größtenteils nur zeilenbasierte Konflikterkennung und bieten daher keine ausreichende Unterstützung für Erkennung und Resolution von Konflikten bei der Versionierung von Softwaremodellen, die eine graphenbasierte Form aufweisen.

Das Ziel dieser Arbeit ist die Erarbeitung und Implementierung einer intelligenten, adaptierbaren Konflikterkennung für die Versionierung von Modellen. Es wird ein Rahmenwerk geschaffen, das out-of-the-box einen verwendbaren Vergleichs- und Konflikterkennungsalgorithmus für Modelle bietet und bei Bedarf durch die Erstellung spezifischer Beschreibungen für eine konkrete Modellierungssprache oder -domäne adaptiert werden kann. Diese sprachspezifischen Erweiterungen erhöhen die Qualität und Genauigkeit der Konflikterkennung und verhindern dadurch unnötige Konfliktmeldungen und manuelle Eingriffe.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Langer_paper.pdf) and [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Langer_poster.pdf)

*Advised by {{% mention "martina-seidl" %}}, {{% mention "manuel-wimmer" %}}, {{% mention "gertrude-kappel" %}}*