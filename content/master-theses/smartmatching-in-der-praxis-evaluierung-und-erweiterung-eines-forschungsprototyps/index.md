---
authors:
- Dominik Karall
categories: []
date: '2020-05-08 15:44:49+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: SmartMatching in der Praxis - Evaluierung und Erweiterung eines Forschungsprototyps
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in August 2009.

In software projects most of the data is saved in a structured way to simplify the usage of it. These data structures are persisted in relational or XML (Extensible Markup Language) databases. In case of new software releases these data structures have to be modified to save new data or adapted data. The usage of a new technology often implies changes in the data structures as well. If changes are made on the data structure, in most of the cases the old data must be migrated to the new data structure to avoid data loss. This process, called information integration, is a time intensive job, and must be done by experts, who create the mapping rules manually and have to take care of the data structure limitations. With schema matching this process can be solved more efficient by schema matching tools build automatically the mapping rules which can be used to transform the data into a new data structure.

SmartMatcher is a schema matching tool prototype, which has been developed at the Vienna University of Technology. This prototype generates mappings out of a source and target schema with their corresponding training instances. The latest release of the SmartMatcher contains a new internal data structure, which should allow more complex mapping operations in future. The effect of this new data structure regard-ing the quality of mappings has been evaluated in this work. Furthermore, a new feature has been integrated which allows to import existing mappings. With this fea-ture the SmartMatcher will be able to use results from other matching tools to im-prove them. In the past the SmartMatcher was limited to one training instance per schema. Thus, a further feature was implemented, called Multiple Samples. This allows more training instances to be used by the SmartMatcher, and improves the user experience by providing a better clarity of the training instances.

Abstract and paper may be found in our <a class="external" href="http://publik.tuwien.ac.at/showentry.php?ID=184543&amp;lang=2">publication database</a>.

 Download the [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Karall_posters.pdf)

*Advised by {{% mention "manuel-wimmer" %}}, {{% mention "gertrude-kappel" %}}*