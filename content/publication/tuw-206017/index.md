---
abstract: Bug Databases which comprise comprehensive records of bugs and their reparations
  are often used as documentation resources by software developers. If such a database
  is not administrated from the beginning of the software development lifecycle, important
  information is lost. This situation can adversely affect the maintainability and
  quality of the software product. This thesis aims to develop a tool that offers
  the possibility to automatically generate such a bug database afterwards. The necessary
  information is obtained from the source code management system that manages all
  source code files of the software project. The tool is based on techniques for the
  classification of log messages and the determination of corrective maintenance tasks.
  Exemplary bug databases are created for various open-source software projects via
  the developed tool. It is shown that the automatic population of a bug database
  is generally possible. A comparative analysis of existing and automatically generated
  bug databases shows that, by the right configuration of the classification, most
  of the bug reports of already existing databases are also present in the automatically
  generated ones. However, a manual comparison uncovers that compromises must be made
  with respect to some information typically available at a bug report. Via the proposed
  tool, bug databases can be generated for any software project, regardless of programming
  language and development area, as long as the software project makes use of a source
  code management system. The results are stored in a generic output format and can
  be imported into any bug tracking system. This produces a documentation that serves
  developers with additional information (e.g., code samples).
authors:
- Thomas Wagner
date: '2011-01-01'
featured: false
links:
- name: Publik
  url: https://publik.tuwien.ac.at/showentry.php?ID=206017&lang=1
publication_types:
- '7'
publishDate: '2011-01-01'
title: Enhancing Maintainability via Populating a Bug Database by Using Repositories
url_pdf: ''
---