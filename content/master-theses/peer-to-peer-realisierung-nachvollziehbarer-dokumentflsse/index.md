---
advisors:
- martin-bernauer
- gertrude-kappel
authors:
- Florian Sonntag
categories: []
date: '2020-05-11 21:33:22+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Peer-to-Peer Realisierung nachvollziehbarer Dokumentflüsse
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in April 2005.

Traceable Document Flows \[Bern04\] ist ein auf dem BIG-Institut entwickeltes Konzept, das es – wie der Name schon sagt – ermöglicht, zu verfolgen, wohin sich Dokumente im Laufe der Zeit bewegt haben. Von Anwenderseite erhält man so eine Art Dokument-Historie, obwohl die Dokumente und deren Versionen völlig dezentral verwaltet werden.

Im Zuge der Diplomarbeit wird dieses Konzept unter Verwendung der Middleware JXTA \[Jxta04\] als Prototyp \[Tdfs04\] realisiert. Jeder Rechner wird als Peer mit einem Namen, einer Beschreibung und einer eindeutigen Peer ID ausgestattet und kann von anderen Peers im Netzwerk gesucht und, wenn gefunden, angesprochen werden. Die Kommunikation erfolgt bei einfachen Mitteilungen über Broadcasting und bei Mitteilungen, deren Empfang unbedingt gewährleistet sein muss, über eine Pipe, die eine direkte Verbindung zwischen zwei Peers darstellt.

Der Prototyp bietet die Möglichkeit Dokumente und Versionen zu erzeugen und diese mittels der Interaktion Checkin entweder lokal oder remote auf anderen Peers zu platzieren. Weiters ist es möglich, Versionen in andere Versionen hineinzuführen (Merge), sie auf andere Peers zu verschieben (Reallocate) oder sie zu löschen (Delete).

Dokumente können andere Dokumente abonnieren, um das Ereignis zu empfangen, das beim Durchführen einer der oben genannten Interaktionen auf dieses Dokument ausgelöst wird. Das Ereignis wird dabei von Version zu Version weitergeleitet, bis alle Versionen des abonnierenden Dokuments erreicht wurden. JXTA bietet aber auch die Möglichkeit, solche Mitteilungen über das JXTA-Discovery-Service zu verbreiten. Der Vergleich dieser beiden Mechanismen stellt den zweiten Teil der Diplomarbeit dar. Hauptaugenmerk liegt dabei auf der Zuverlässigkeit und Dauer des Ereignisflusses in unterschiedlichen Netzwerken. Möchte man sicherstellen, dass ein Ereignis alle Versionen des abonnierenden Dokuments erreicht, ist erstere Variante zu wählen. Ist einem hingegen wichtig, dass die Verteilung so schnell als möglich unter Inkaufnahme des Nichterreichens mancher Versionen durchgeführt wird, ist dem JXTA-Discovery-Service der Vorzug zu geben.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Sonntag_poster.pdf)