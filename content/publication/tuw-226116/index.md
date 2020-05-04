---
abstract: Web applications offer a multitude of configuration switches that need to
  be set correctly. In case of a single product it is feasible to manage the configuration
  files with the source code in a version control system. However, in case of a product
  line with many similar products it is necessary to have means to manage the configurations
  separately. Furthermore it is desirable to be able to apply the configurations automatically,
  because a manual configuration is error prone and time consuming. The aim of this
  thesis was the creation of a system that supports (and partially automates) the
  configuration management of software product lines of enterprise web applications.
  It should support the storage of configuration information in machine readable form
  and provide a tool that is able to apply those configurations automatically. Furthermore
  the tool should be integrable in the build automation system. In a first step the
  products of the product line were analyzed and all existing configuration switches
  were documented and categorized. Afterwards an object model was abstracted which
  is able to cover the configurations of the product line. A focus was laid on extensibility
  and the special requirements of software product lines. Based on the model a configuration
  tool was developed which is able to configure each product. Finally the tool was
  integrated in the automatic build process of the continuous integration server.
  Thus, it is now possible to build all products auto- matically and deploy them correctly
  configured. Moreover the required time to configure a product was considerably reduced.
  The measured time saving between automated and manual installations ranges from
  17 to 40 minutes (depending on the complexity of the installation).
authors:
- Alexander Ahammer
date: '2013-01-01'
featured: false
links:
- name: Publik
  url: https://publik.tuwien.ac.at/showentry.php?ID=226116&lang=2
publication_types:
- '7'
publishDate: '2013-01-01'
title: Managing and Automating Configuration in Software Product Lines for Enterprise
  Web Applications
url_pdf: ''
---