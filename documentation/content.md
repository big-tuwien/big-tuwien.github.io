# Aufbereitung von Inhalten

## Strukturierung

Alle Inhalte der Seite befinden sich im `content` Verzeichnis. Die Ordner auf der ersten Ebene werden dabei zu 
Gruppierungszwecken eingesetzt. So werden beispielsweise alle News-Einträge im `content/news` Ordner oder die Mitglieder 
im `content/people` Ordner gesammelt. Dieses Schema gilt für alle Ordner bis auf `content/home`, in welchem sich die 
Informationen für die Hauptseite befinden und `content/teaching`, wo die Inhalte für die Teaching Unterseite vorgefunden 
werden können. Die Datei `privacy.md` beinhält die privacy policy. 

In den Ordnern befindet sich meist eine `index.md` oder `_index.md` Datei. Diese ist für die interne Strukturierung 
vorgesehen und kann im Normalfall ignoriert werden.

Der Kern der Seite sind die Hauptseite (`content/home`) und die Teachingseite (`content/teaching`), 
welche in einzelne Segmente, sogenannte "widgets", unterteilt wurde. 

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

Allgemein wird das Format *Markdown* für das Erstellen von Inhalten genutzt. Markdown bietet die Möglichkeit Text
ohne weitere Konvertierung formatiert darzustellen. So wird zum Beispiel der Text `*dd*` kursiv formatiert, 
oder `# Heading` als Überschrift. Ein Ziel von Markdown ist, dass schon die Ausgangsform ohne weitere Konvertierung 
leicht lesbar ist.

Ein Guide, wie Inhalte mit Markdown formatiert werden können, wird in der offiziellen Dokumentation von `hugo-academic`
angeführt: [Writing content with Markdown, LaTeX, and Shortcodes](https://sourcethemes.com/academic/docs/writing-markdown-latex/)

### Shortcodes

Neben der Formatierung durch Markdown, bietet `hugo-academic` noch einige Zusatzfunktionen, sogenannte *Shortcodes*,
mit welchen das Einfügen von gewissen Inhalten wie etwa Bildern vereinfacht werden soll.

#### Personen verlinken

Personen, welche unter `content/people` angelegt wurden, können sehr einfach in einer Inhaltsseite verlinkt werden.
Der Code `{{% mention "max-muster" %}}` würde beispielsweise auf die Person unter `content/people/max-muster` 
verweisen. Anstelle dieses Shortcodes wird [Max Muster]() eingesetzt.
