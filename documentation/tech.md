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

Gehostet wird die Seite über [GitHub Pages](https://pages.github.com/). Der Inhalt der master branch wird unter
https://big-tuwien.github.io/ eingebunden.

### Aktualisieren von hugo-academic

Es befindet sich ein Script zum updaten von `hugo-academic` im Hauptverzeichnis.

Aktualisierungen des Themes sollten generell nur im Notfall durchgeführt werden. Während der Entwicklung wurden einige
Layouts des Themes überschrieben, da anpassungen notwendig waren. Bei einer Aktualisierung wäre es möglich, dass die
angepassten Files mit der neueren Version inkompatibel sind und Fehler entstehen.

## Script zur Datenaktualisierung

Um die Webseite mit dem Datenstand aus TISS und der Publikationsdatenbank abzugleichen, wurde ein Python script geschrieben,
welches sich sich im Ordner `scripts/fetch` befindet. Das script bietet Funktionen um Mitgliederdaten, Kursinformationen 
und Publikationen zu laden.

Das script sollte stets aus dem eigenen Folder (`scripts/fetch` und nicht z.B. aus dem Hauptverzeichnis) aufgerufen 
werden, da sonst die Variablen `config`, `group_config` und `base_dir` angepasst werden müssen. Es wurde mithilfe eines
argument parsers sichergestellt, dass einfach über das CLI mit dem script interagiert werden kann. Daher können mithilfe
des Aufrufs `fetch.py -h` die möglichen Optionen angezeigt werden.

### Speicherorte

* Mitgliederdaten: `content/people`
* Kursdaten: `data/teaching/courses`
* Publikationen: `content/publication`

### Konfiguration

Das script verfügt über zwei Konfigrutationsdateien:
* `config.yml` verfügt über die Konfiguration für courses und publications. Es können Blacklists definiert werden,
  und Namen, bei denen es Unterschiede zwischen dem TISS und publik gibt, können umgewandelt werden. Die Basis aller
  Blacklisten ist immer die Groups Liste.
* `groups.yml` verfügt über die Namen der Mitglieder und Gruppierungen in der *people* Sektion auf der Hauptseite.
  **Die Namen müssen mit den Namen aus dem TISS übereinstimmen und die Person muss in der TISS BIG Organisationseinheit 
  eingetragen sein, sonst werden keine Daten für diese Personen geladen. Das bedeutet auch, das Gertude Kappel nicht auf 
  Gerti Kappel umbenannt werden kann, sofern es nicht so im TISS steht.**
  Die `default` Gruppe wird auf alle Personen angewant, die nicht explitzit in der Liste aufscheinen.

## CI/CD

Um das Aktualisieren der Daten zu vereinfachen, wird dieser Prozess mithilfe von 
[GitHub Actions](https://github.com/features/actions) automatisiert. Die Konfiguration der Workflows ist unter
`.github/workflows` einsehbar.

### Automatisches Bauen der Webseite

Bei jedem push auf die `content` branch werden die publications von [publik](https://publik.tuwien.ac.at/) geladen, 
die Seite mit Hugo gebaut und auf den master branch gepusht. Existierende Publikationen im `content/publication` 
werden dabei nicht überschrieben.

### Automatische Datenaktualisierung

Zu einem festgelegten Zeitpunkt wird ein scheduled job ausgeführt, der alle Member- und Kursdaten aktualisiert und auf
die content branch gepusht.
