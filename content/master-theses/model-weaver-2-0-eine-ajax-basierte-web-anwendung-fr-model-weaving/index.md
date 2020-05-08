---
authors:
- Jeremy Solarz
categories: []
date: '2020-05-08 15:28:14+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Model Weaver 2.0 - eine AJAX-basierte Web-Anwendung für Model Weaving
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in January 2008.

Modellgetriebene Softwareentwicklung (MDSD) soll dabei helfen, Softwaresysteme hinsichtlich ihrer Komplexität zu vereinfachen und ihre Qualität zu steigern. Dazu werden Werkzeuge benötigt, welche den Benutzer dabei unterstützen. Ein Bestandteil von MDSD ist Model Weaving, welches für eine Vielzahl von Anwendungen eine Voraussetzung darstellt. Unter anderem liefert Model Weaving die nötigen Informationen, um daraus Modelltransformationen abzuleiten. Es ist möglich, mehrere Modelle durch diese Modelltransformation in ein Modell zusammen zu führen, Modelle in ihrem Informationsumfang zu erweitern und dergleichen. Herkömmliche Ansätze, wie der ATLAS Model Weaver (AMW) der ATLAS Group, sind als Rich-Client-Anwendung implementiert, was nicht immer von Vorteil ist. Zusätzliche Ressourcen auf der Client-Seite und eine Installation beim Benutzer zählen dazu. Da der AMW Bestandteil des Eclipse Modelling Frameworks ist und nicht jede Version miteinander kompatibel ist, kann es hier zu unerwarteten Schwierigkeiten kommen. Auch in der modellgetriebenen Softwareentwicklung haben sich Plattformen entwickelt, welche den Austausch von Modellen erleichtern sollen. Diese als „Model Repositories“ bezeichneten Plattformen sollen Grundgerüste für die Modellentwicklung bereitstellen. Hier wäre es hilfreich, Verbindungen zwischen den einzelnen „Repositories“ zu schaffen. Ziel dieser Arbeit ist es, basierend auf dem MetaModelbrowser von Jürgen Flandorfer, eine Anwendung zu entwickeln, welche das Thema Model Weaving aufgreift und versucht, dieses mit dem Web zu verbinden. Dies hat den Vorteil, dass dem Benutzer der Umgang mit dem Web vertraut ist, somit kein zusätzlicher Lernaufwand entsteht. Probleme bezüglich Performanz auf der Clientseite werden vermieden und ein leichtgewichtiger, ressourcensparender Client wird geschaffen, welcher keine Installation mehr benötigt. Da eine weitgehend eigenständige Weaving Umgebung geschaffen wird, kommt es nicht zu einem Zusammenspiel mehrerer Softwarekomponenten, wie es beim AMW der Fall ist. Modelle können zentral am Server abgelegt werden. Dies ermöglicht ein gemeinsames Arbeiten an Modellen. Mit einer Funktion des MetaModelbrowsers können Modelle anhand einer URL eingebunden werden. Somit ist es möglich, Model Repositories in den Weaving Prozess mit einzubeziehen. Als Alternative zu den Eclipse basierten Model Weaving Ansätzen soll also eine webbasierte Anwendung geschaffen werden, mit deren Hilfe die Probleme der herkömmlichen Ansätze vermieden werden können.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Solarz_paper.pdf) and [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Solarz_poster.pdf)

*Advised by {{% mention "michael-strommer" %}}, {{% mention "gertrude-kappel" %}}*