---
abstract: 'Information integration has a long history in computer science1. It has
  started with the integration of database schemas in the early eighties. With the
  rise of the SemanticWeb and the emerging abundance of ontologies, the need for an
  automatic information integration increased further.  Information integration in
  general and automatic information integration in particular is a huge and challenging
  research area. One of the main problems is handling semantic heterogeneity and schema
  heterogeneity. Manually finding the semantically overlapping parts of schemas is
  a tedious problem. Furthermore, writing integration code is a labor intensive, error-prone,
  and cumbersome task. A lot of approaches have already been developed to automate
  this work. Nevertheless, not all integration problems have been solved so far. Matching
  tools are used to automatically find similarities between schemas. The results of
  these tools are simple correspondences. Based on these correspondences, one is able
  to write integration code. However, the simple correspondences are just suggestions
  and must be verified manually. Hence, the completeness and correctness of the resulting
  correspondences may not be assured. Furthermore, it is not possible to automatically
  derive transformation code for all found simple correspondences.  In order to write
  transformation code, different kinds of transformation languages have been developed.
  The produced code is too customized for a specific type of schema to be easily reused
  for other integration problems. Hence, to the best of our knowledge, there exists
  no transformation language to develop reusable transformation patterns for different
  kinds of heterogeneity problems.  This thesis addresses the heterogeneity problems,
  as well as the lack of reusable transformation code, and the need for establishing
  correct and complete correspondences between schemas. The first two problems are
  tackled by developing an executable declarative mapping language, which is able
  to cope with the core of schema heterogeneity problems. In contrast to simple correspondences,
  this mapping language is able to express more constraints. Based on these more expressive
  mappings, the execution code is automatically derived. The third problem is tackled
  by a self-tuning, iterative matching approach. This approach is based on the developed
  mapping language. Mapping strategies are responsible for the application of mapping
  operators. Based on the executable mapping suggestion, completeness and correctness
  are achieved for a provided set of instance models by a testdriven approach. These
  instance models are used to evaluate the produced mapping model. The prototype of
  this self-tuning approach is called SmartMatcher.  1Laura Haas. Beauty and the Beast:
  The Theory and Practice of Information Integration. In 11th International Conference
  on Database Theory, Springer LNCS 4353, 2007, pp. 28-43.'
authors:
- Horst Kargl
date: '2008-01-01'
featured: false
links:
- name: Publik
  url: https://publik.tuwien.ac.at/showentry.php?ID=168069&lang=1
publication_types:
- '7'
publishDate: '2008-01-01'
title: Smart Matching - An Approach for the Automatic Generation of Executable Schema
  Mappings
url_pdf: http://publik.tuwien.ac.at/files/PubDat_168069.pdf
---