---
authors:
- Manuel Wimmer
categories: []
date: '2020-05-08 18:02:41+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: From Mining to Mapping and Roundtrip Transformations – A Systematic Approach
  to Model-based Tool Integration
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in March 2008.

Model-Driven Engineering (MDE) gains momentum in academia as well as in practice. A wide variety of modeling tools is already available supporting different development tasks and advocating different modeling languages. In order to fully exploit the potential of MDE, modeling tools must work in combination, i.e., a seamless exchange of models between different modeling tools is crucial for MDE. Current best practices to achieve interoperability use model transformation languages to realize necessary mappings between the metamodels defining the modeling languages supported by different tools. However, the development of such mappings is still done in an ad-hoc and implementation-oriented manner which simply does not scale for large integration scenarios. The reason for this is twofold. First, various modeling languages are not based on metamodeling standards but instead define proprietary languages rather focused on notational aspects. And second, existing model transformation languages both do not support expressing mappings on a high-level of abstraction and lack appropriate reuse mechanisms for already existing integration knowledge.

This thesis contributes to the above mentioned problems. It proposes a comprehensive approach for realizing model-based tool integration, which is inspired from techniques originating from the field of database integration, but employed in the context of MDE. For tackling the problem of missing metamodel descriptions, a semi-automatic approach for mining metamodels and models from textual language definitions is presented, being a prerequisite for the subsequent steps which are based on metamodels and models, only. For raising the level of abstraction and for ensuring the reuse of mappings between metamodels, a framework is proposed for building, applying, and executing reusable mapping operators. To demonstrate the applicability of the framework, it is applied to the definition of mapping operators which are intended to resolve typical structural heterogeneities occurring between the core concepts of metamodels. Finally, for ensuring roundtrip capabilities of transformations, two approaches are proposed evolving non-roundtripping transformations with roundtrip capabilities.

Abstract and paper may be found in our <a class="external" href="http://publik.tuwien.ac.at/showentry.php?ID=141768&amp;lang=2">publication database</a>.

*Advised by {{% mention "gertrude-kappel" %}}*