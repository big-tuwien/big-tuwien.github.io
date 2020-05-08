---
authors:
- Petra Brosch
categories: []
date: '2020-05-08 18:02:35+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Conflict Resolution in Model Versioning
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in July 2012.

In most engineering disciplines, models are built as pragmatic, yet precise abstractions of huge systems. The model building process requires multiple people jointly elaborating on artifacts, which are analyzed, used to communicate among stakeholders, and act finally as construction plan for realizing the modeled system. In the field of software engineering, modeling languages such as the _Unified Modeling Language_ (UML) provide multiple diagrams to describe various viewpoints of a system in a concrete graphical notation. While the code-centric software engineering discipline adopted those models as visual language for describing the system under study, the increasing complexity of modern software systems accompanied by ever shorter time to market constraints has asked for new techniques. The upcoming _Model-Driven Engineering_ (MDE) approach aims at additionally exploiting models to automatically generate executable code. This paradigm shift lifts models to first-class citizens within the whole engineering process, effectively shaping the primary artifact of change undergoing the collaborative refinement from informal sketches to blueprints. This upgrowth intrinsically demands tool support for managing the models‘ history including merging of parallel evolved models. Optimistic versioning systems, which are already successfully applied for the management of source code, handle both issues. However, applying those systems to models fails due to the models‘ graph-based structure. Consequently, first dedicated model versioning systems emerged. Although current model versioning systems provide decent conflict detection facilities, they (1) ignore the graphical representation of the models, and (2) neglect conflict resolution by totally shifting the responsibility to the user. Yet, the central role of models unifying the human-centric, collaborative abstraction and design process with the computation-centric process of generating executable systems, demands proper mechanisms to foster validity and quality of the merged model.

In this thesis, we first analyze specifics of model versioning and elaborate on the notion of conflict to improve conflict resolution respecting the central role of models. To cope with the human-centric aspect, we present a conflict aware merge strategy to calculate a tentatively merged _conflict diagram_ as accelerator for conflict resolution retaining the graphical representation of the model. The conflict diagram unifies non-conflicting changes and materializes merge conflicts in form of annotations, rendering a coherent picture of the model’s evolution. To further support the conflict resolution process, we elaborate on a _conflict resolution recommender system_ on top of the conflict diagram, which recommends automatically executable conflict resolution patterns. Finally, to satisfy validity conditions of the computation-centric aspect, we establish a _formal framework_ based on graph transformation theory, to showcase the feasibility of our approach.

Abstract and paper may be found in our <a class="external" href="http://publik.tuwien.ac.at/showentry.php?ID=208975&amp;lang=2">publication database</a>.

*Advised by {{% mention "martina-seidl" %}}, {{% mention "gertrude-kappel" %}}*