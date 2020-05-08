---
authors:
- Konrad Wieland
categories: []
date: '2020-05-08 15:45:07+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Conflict-tolerant Model Versioning
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in December 2011.

Model-driven software engineering (MDSE), which has recently gained momentum in academia as well as in industry, changed the way in which modern software systems are built. In MDSE, the task of programming, i.e., writing code in a textual programming language, is replaced by modeling in a language such as the Unified Modeling Language (UML). The powerful abstraction mechanisms of models are not only used for documentation purposes, but also for compiling executable code directly out of models. With the rise of MDSE, several problems solved for traditional software engineering became urgent again because well established solutions are not directly transferable from code to models. Among others, the collaborative development of models is currently only limited supported by modeling tools and, consequently, it is mostly a one-(wo)man show. Especially in the field of model versioning, which supports the asynchronous modification of modeling artifacts by multiple developers, only first solutions start to emerge.

The urgent need for a suitable infrastructure supporting effective model versioning has been widely recognized by researchers as well as practitioners. Currently, however, there is a lack of empirical studies on the needs of software developers in practice concerning the collaborative development of software systems. The first contribution of this thesis tackles this problem and provides an extensive survey about versioning in practice by the means of an online questionnaire and qualitative expert interviews. One result of the empirical study shows that conflicts due to parallel modifications are considered harmful and, thus, developers try to avoid them. Conflicts, however, should not be seen as negative result of collaboration but as chance for discussing ideas and for improving the system under development. As consequence, the second contribution is a conflict-tolerant model versioning approach, where the developers may commit their changes in the central repository without worrying about possible conflicts. This approach merges two or more parallel versions by applying dedicated merge rules and, by this, it incorporates all modifications of the developers. This builds a good basis for discussing and resolving conflicts collaboratively. Finally, when resolving conflicts a high degree of user interaction is required. When setting models under version control with state-of-the art tools, however, conflicts are hardly accessible for the users. Also the empirical study has shown, that current version control systems lack for a dedicated representation and visualization. Moreover, user support is required to better understand the reasons behind the conflicting changes. The third contribution tackles these deficiencies by visualizing occurred conflicts in terms of model annotations and enriching them automatically with additional meta information to better understand the parallel evolution of the model under development. The implemented prototype is evaluated by means of a quasi-experimental study, which demonstrates the advantages of developing models in a collaborative manner.

Abstract and paper may be found in our <a class="external" href="http://publik.tuwien.ac.at/showentry.php?ID=209022&amp;lang=2">publication database</a>.

*Advised by {{% mention "martina-seidl" %}}, {{% mention "manuel-wimmer" %}}, {{% mention "gertrude-kappel" %}}*