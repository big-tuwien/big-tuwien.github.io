---
authors:
- Simon Tragatschnig
categories: []
date: '2020-05-08 15:44:57+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Ein Ansatz zur Auflösung von Konflikten bei der Versionierung von Modellen
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in February 2009.

In der modernen Softwareentwicklung werden Modelle nicht nur zur Dokumentation eingesetzt sondern auch zur Generierung von Quellcode. Syntaxfehler und Inkonsistenzen im Modell wirken sich daher direkt auf den Quellcode aus. Bearbeitet nur ein Entwickler ein Modell, so kann ein zumindest in sich konsistentes Modell durch die von der Entwicklungsumgebung zur Verfügung gestellten Werkzeuge gewährleistet werden. Arbeiten jedoch mehrere Entwickler kollaborativ an einem Modell, was der realistischere Fall ist, muss dieses unter Versionskontrolle (version control system, VCS) gestellt werden. Herkömmliche textbasierte Ansätze zur Versionierung sind für graphische Modelle jedoch nicht ausreichend.

Die Verwendung von konventionellen VCS zur Versionierung von Modellen bringt zwei grundlegende Probleme mit sich. Das erste Problem bezieht sich auf die auftretenden Konflikte zwischen zwei Modellversionen, z.B. wenn mehrere Entwickler gleichzeitig dasselbe Modellelement ändern. Diese Konflikte müssen durch die Entwickler manuell aufgelöst werden, da für eine Zusammenführung der Änderungen keine Werkzeugunterstützung existiert. Treten bei der manuellen Zusammenführung der Änderungen Fehler auf, hat dies dierekten Einfluss auf den generierten Quellcode. Das zweite Problem bezieht sich auf Information, die während der Konfliktauflösung entsteht, aber für zukünftige ähnliche Konfliktsituationen nicht gespeichert wird und daher nicht wiederverwendet werden kann. Diese Information könnte jedoch dem Entwickler bei späteren Konfliktauflösungen hilfreich sein. Außerdem könnten auf Basis dieser Information über mögliche Konfliktsituationen Entwurfsrichtlinien für die Erstellung eines Modells vorgegeben werden.

Der in dieser Arbeit vorgestellte Ansatz zur Konfliktauflösung ermöglicht eine Beschreibung von Auflösungsstrategien für syntaktische und statisch semantische Konflikte. Zur Beschreibung der syntaktischen Konflikte und deren Auflösung wird eine modellbasierte, deskriptive Sprache vorgestellt. Zur Auflösung der statisch semantischen Konflikte werden Graph-Produktionsregeln bzw. Muster mittels OCL genutzt.

Durch den modellbasierten Ansatz der Sprachdefinition für die Beschreibung der Auflösungsstrategien ist eine einfache und flexible Erweiterung bzw. Änderung der Strategien möglich. Die gemeinsame Struktur bildet die Grundlage für eine Protokollierung der Benutzerentscheidungen. Aus diesen können zusätzliche Informationen zur Unterstützung des Benutzers bei der Entscheidungsfindung der passenden Auflösungsstrategie gewonnen werden. Die Prüfung auf Einhaltung von Entwurfsrichtlinien ist ebenfalls möglich. Durch die erhöhte Qualität der zusammengeführten Modellversionen werden beim generierten Code Fehler zur Compile- und Laufzeit reduziert.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Tragatschnig_paper.pdf) and [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Tragatschnig_poster.pdf)

*Advised by {{% mention "martina-seidl" %}}, {{% mention "manuel-wimmer" %}}, {{% mention "gertrude-kappel" %}}*