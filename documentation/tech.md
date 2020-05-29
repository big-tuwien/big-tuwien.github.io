# Technische Details und Wartung

## Technische Konzepte

Zur Umsetzung der Seite wird der SSG [Hugo](https://gohugo.io/) verwendet. In Hugo werden Layout-Templates definiert,
die später mit Font-Matter Metadaten befüllt werden. So sind Inhalte und Layout abekapselt und die Komponenten können 
einfach wiederverwendet werden. Die Hugo-Ordnerstruktur kann [hier](https://gohugo.io/getting-started/directory-structure/) 
nachgeschlagen werden. Alle weiteren Informationen können der [Dokumentation](https://gohugo.io/documentation/)
entnommen werden.

Neben Hugo kommt auch ein entsprechendes Theme zum Einsatz, welches viele vorgefertigte Funktionen und Komponenten mit
sich bringt. Die Dateien des `hugo-academic` themes sind unter `themes/academic` anzufinden. Diese sollten allerdings 
nicht bearbeitet werden, da das Theme als `git submodule` eingebunden ist.  
Sollen gewisse Komponenten wie etwa layouts abgeändert werden, so müssen diese aus dem `themes/academic` Ordner an den
korrespondierenden Platz in der eigenen Codebase verschoben werden. Beispielsweise müsste 
`themes/academic/layouts/404.html` nach `layouts/404.html` verschoben werden um bearbeitet werden zu können.

Die Webseite wurde mit Hugo `0.68.3` entwickelt und getestet. Sollten bei neueren Hugo-Versionen Fehler auftreten,
könnte dies auf Inkompatibilität mit der Version des `hugo-adacemic` Themes zurückzuführen sein.

### Aktualisieren von hugo-academic

Es befindet sich ein Script zum updaten von `hugo-academic` im Hauptverzeichnis.

Aktualisierungen des Themes sollten generell nur im Notfall durchgeführt werden. Während der Entwicklung wurden einige
Layouts des Themes überschrieben, da anpassungen notwendig waren. Bei einer Aktualisierung wäre es möglich, dass die
angepassten Files mit der neueren Version inkompatibel sind und Fehler entstehen.

## Script zur Datenaktualisierung

Um die Webseite mit dem Datenstand aus TISS und der Publikationsdatenbank abzugleichen, wurde ein Python script geschrieben,
welches sich sich im Ordner `scripts/fetch` befindet.



## CI/CD

### Automatisches Bauen der Webseite

### Automatische Datenaktualisierung
