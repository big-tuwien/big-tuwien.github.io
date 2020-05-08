---
authors:
- Thomas Halmetschlager
categories: []
date: '2020-05-08 14:38:44+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Synchronous Collaborative Modeling for the Eclipse Modeling Framework
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in July 2011.

The high complexity of modern software makes it unavoidable to develop software with the help of graphical, model based editors. Software models serve not only as documentation or as a rough system overview. They are also the fundament to generate an executable system.

The larger the application the more persons are involved in the design and development process. Simultaneous changes on a model are very common. With these concurrent changes conflicts can occur.

There is a need of interpersonal communication to solve appearing questions and avoid misunderstandings. Specially in the early stage of software development diversities in interpretation may occur because the semantics of models may be interpreted differently. To avoid such problems the communication channels within the team should be supported as much as possible. With good communication it should be possible to achieve a consolidated solution of the problem in a collaborative way.

Within this thesis ways and means are sought to enable interactive model-driven software development with the Eclipse Modeling Framework. It turned out that there are already several approaches for this interactive development method.

These budding candidates where reviewed and analyzed. Unfortunately each of the tested systems had some disadvantages or they were not mainly designed for model-driven software development. Using them for serious software development would not have been possible.

As soon as the analysis of various existing approaches was finished a list of requirements has been created. The search for a tool that matches the requirements as good as possible and that can be extended easily was started and finished with an acceptable result.

Therefore the implementation part consists of an extension of a existing tool. The chosen tool is CDO, ”Connected Data Objects“, a plugin for Eclipse. CDO was selected because it is the best match to our requirements and is supported by a very competent development team. We think we found the optimal candidate to develop a sustainable solution.

Within this thesis we developed a functionality that enables the user to merge two branches of the versioning system, CDO.

Abstract and paper may be found in our <a class="external" href="http://publik.tuwien.ac.at/showentry.php?ID=199046&amp;lang=2">publication database</a>.

 Download the [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Halemtschlager_poster.pdf)

*Advised by {{% mention "martina-seidl" %}}, {{% mention "konrad-wieland" %}}, {{% mention "philip-langer" %}}, {{% mention "gertrude-kappel" %}}*