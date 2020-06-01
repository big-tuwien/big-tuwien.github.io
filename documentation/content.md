# Aufbereitung von Inhalten

## Strukturierung

Alle Inhalte der Seite befinden sich im `content` Verzeichnis. Die Ordner auf der ersten Ebene werden dabei zu 
Gruppierungszwecken eingesetzt. So werden beispielsweise alle News-Einträge im `content/news` Ordner oder die Mitglieder 
im `content/people` Ordner gesammelt. Dieses Schema gilt für alle Ordner bis auf `content/home`, in welchem sich die 
Informationen für die Hauptseite befinden und `content/teaching`, wo die Inhalte für die Teaching Unterseite vorgefunden 
werden können. Die Datei `privacy.md` beinhält die privacy policy. 

In den Ordnern befindet sich meist eine `index.md` oder `_index.md` Datei. Diese ist für die interne Strukturierung 
vorgesehen und kann im Normalfall ignoriert werden.

Inhalte können entweder als Ordner, oder als Datei angelegt werden. Soll beispielsweise ein Projekt mit dem Namen
`Projekt A` angelegt werden, so kann entweder die Datei `content/project/projekt-a.md` oder eine Index-Datei im
entsprechenden Unterordner `content/project/projekt-a/index.md` angelegt werden. Der zweite Ansatz macht besonders dann
Sinn, wenn zusätzliche Dateien wie Bilder in dem Ordner abgelegt werden sollen, die dann später eingebunden werden.
Ein Bild würde in diesem Beispiel etwa unter `content/project/projekt-a/image.jpg` platziert werden.

Um den Überblick zu behalten, können Dateien, die nicht länger aktuell sind, wie etwa die News-Einträge der letzten
Jahre, ein den `archive` Ordner verschoben werden. Diese wird für jeden Inhaltstyp separat geführt. So befindet 
sich beispielsweise der `archive` Ordner für News-Beiträgt unter `content/news/archive`.  
**Achtung:** Für `people` ist dieses Konzept **NICHT** anwendbar. Alle Inhalte müssen sich im Hauptordner befinden.

Der Kern der Seite sind die Hauptseite (`content/home`) und die Teachingseite (`content/teaching`), 
welche in einzelne Segmente, sogenannte *widgets*, unterteilt wurde. Weitere Informationen zu *widgets* können
dieser Seite entnommen werden: [Create a widget page](https://sourcethemes.com/academic/docs/managing-content/#create-a-widget-page)

### Zuordnungen

| Name des Ordners | Inhalt |
|------------------|---------------|
| master-thesis | [Master Theses](https://big-tuwien.github.io/teaching/masters/) |
| news | [News](https://big-tuwien.github.io/#news) |
| offered-topic | [Offered Topics](https://big-tuwien.github.io/teaching/offered/) |
| people | [People](https://big-tuwien.github.io/#people) |
| phd-thesis | [PhD Theses](https://big-tuwien.github.io/teaching/phds/) |
| project | [Projects](https://big-tuwien.github.io/#projects) |
| publication | [Publications](https://big-tuwien.github.io/publication/) |
| seminar | [Recent & Upcoming Seminars](https://big-tuwien.github.io/teaching/seminars/) |
| visitors | [Visitors and Friends](https://big-tuwien.github.io/visitors/) |

### Konfigurationsdateien

Gewisse Daten, wie etwa wie die Informationen der `Contact` Sektion, oder die Menüleiste müssen in den Konfigurationsdateien
`config/_default/config.toml`, `config/_default/params.toml`, `config/_default/menus.toml` angepasst werden.

## Dateiaufbau

Jede Markdown Datei (`.md`) besteht aus zwei Segmenten: einem Metadatensegment (auch *Front Matter*) und einem Inhaltssegment. 

### Front-Matter (Metadaten)

Durch Front-Matter ist es möglich, seitenspezifische Informationen anzugeben. Diese werden am Kopf eines Markdown-Files 
angegeben. So ist es einfach möglich Daten wie den Titel der Seite oder das Erstellungsdatum festzulegen oder anzupassen.
Die Informationen werden später in die Seite eingesetzt. 

Laut der Dokumentation des Tools, wird für Inhaltsdateien das [YAML](https://learnxinyminutes.com/docs/yaml/) Format und 
für Konfigurationsdateien und Widgetdateien das [TOML](https://learnxinyminutes.com/docs/toml/) Format eingesetzt.
Als Grund wird angegeben, dass TOML endnutzerfreundlicher ist, aber viele Markdown-Editors hauptsächlich YAML unterstützen.

Wenn ein Content-File die Front-Matter zwischen drei Minus-Zeichen `---` definiert, wird das YAML-Format verwendet. 
Anderenfalls werden die Front-Matter-Variablen zwischen drei Plus-Zeichen `+++` angelegt, wodurch das TOML-Format zum
Einsatz kommt.

#### YAML

```yaml
---
date: 2017-12-01
title: My first blog post
---
```

#### TOML

```toml
+++
date = 2017-12-01
title = "My first blog post"
+++
```

Weitere Informationen zum Thema Front-Matter können der offiziellen Dokumentation des genutzten `hugo-academic` Themes
entnommen werden: [Front Matter](https://sourcethemes.com/academic/docs/front-matter/).

Auch Erläuterungen der häufig zum Einsaz kommenden Metadaten wird in der `hugo-academic` Dokumentation angeführt: 
[Wichtige Metadaten](https://sourcethemes.com/academic/docs/managing-content/#introduction)

### Inhalte

Allgemein wird das Format *Markdown* für das Erstellen von Inhalten genutzt. Markdown bietet die Möglichkeit, Text
ohne weitere Konvertierung formatiert darzustellen. So wird zum Beispiel der Text `*dd*` kursiv formatiert, 
oder `# Heading` als Überschrift. Ein Ziel von Markdown ist, dass schon die Ausgangsform ohne weitere Konvertierung 
leicht lesbar ist.

Ein Guide, wie Inhalte mit Markdown formatiert werden können, wird in der offiziellen Dokumentation von `hugo-academic`
angeführt: [Writing content with Markdown, LaTeX, and Shortcodes](https://sourcethemes.com/academic/docs/writing-markdown-latex/)

### Shortcodes

Neben der Formatierung durch Markdown, bietet `hugo-academic` noch einige Zusatzfunktionen, sogenannte *Shortcodes*,
mit welchen das Einfügen von gewissen Inhalten wie etwa Bildern vereinfacht werden soll.

Die verfügbaren Shortcodes können hier eingesehen werden: 
[Writing content with Markdown, LaTeX, and Shortcodes](https://sourcethemes.com/academic/docs/writing-markdown-latex/)  
Alle Informationen zu den folgenden Shortcodes können auch auf der eben genannten Seite nachgelesen werden.

#### Personen verlinken

Personen, welche unter `content/people` angelegt wurden, können sehr einfach in einer Inhaltsseite verlinkt werden.
Der Code `{{% mention "max-muster" %}}` würde beispielsweise auf die Person unter `content/people/max-muster` 
verweisen. Anstelle dieses Shortcodes wird [Max Muster]() eingesetzt.

#### Bilder einbinden

Bilder sollten entweder in den statischen Medienbibliothek unter `static/img`, oder, wenn möglich, 
im eigenen Ordner der Seite, wie etwa `content/news/mein-newsbeitrag`, platziert werden.

Bild aus der Medienbibliothek einbinden:
```
{{< figure library="true" src="image.jpg" title="A caption" lightbox="false" >}}
```

Bild aus dem eigenen Ordner der Seite einbinden:
```
{{< figure src="image.jpg" title="A caption" lightbox="false" >}}
```

Der Parameter *lightbox* gibt dabei an, ob das Bild bei einem Klick hervorgehoben werden soll.

#### Links

Im Zuge einer Verlinkung können die Shortcodes *ref* und *relref* verwendet werden.

```markdown
[I'm a link](https://www.google.com)
[A post]({{< ref "/post/my-page-name/index.md" >}})
[A publication]({{< ref "/publication/my-page-name/index.md" >}})
[A project]({{< ref "/project/my-page-name/index.md" >}})
[A relative link from one post to another post]({{< relref "../my-page-name/index.md" >}})
[Scroll down to a page section with heading *Hi*](#hi)
```

#### Statische Dateien

Um PDFs oder andere Dateien einzubinden, müssen diese erst zu der statischen Medienbibliothek unter `static/files` 
hinzugefügt und dann wie folgt eingefügt werden:

```
{{% staticref "files/cv.pdf" "newtab" %}}Download my CV{{% /staticref %}}
```

Das Argument `"newtab"` ist optional und öffnet den Link in einem neuen Tab.
