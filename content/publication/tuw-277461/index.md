---
abstract: Software as a Service (SaaS) as an alternative to locally installed Software
  is constantly gaining popularity through new, modern web technologies and flexible
  subscription payment models. Providers introduce their solutions to specific markets
  quickly and efficiently using agile development models and continue further development
  after release. Should the provider wish to reach new markets and user bases, their
  software is required to implement new requirements and support specific configurations
  for each user at runtime even though it was seldom specifically designed for this
  purpose. This is the starting point for this thesis, which evaluates the applicability
  of existing approaches for managing variability in software in the context of SaaS.
  For the most common class of SaaS already in the operational phase, Java web applications,
  a method is developed to implement new requirements in the existing implementation.
  For this purpose, the existing feature set of the application is reconstructed and
  translated together with new features to a variability model. Existing legacy code
  is refactored and new tests introduced to prevent further degradation before SaaS-applicable
  variability implementation techniques are applied. Additionally, a meta model is
  implemented to support different configurations for users at runtime and centrally
  manage both existing and newly introduced variability. Newly created or adapted
  user journey tests ensure the continued correctness of the application. An exemplary
  application of the method is performed within a case study, which involved an existing
  accounting SaaS being extended to allow the purchasing of a point-of-sale extension
  as a standalone feature for new users. The successful implementation and delivery
  to the customer confirms the practicality of the method.
authors:
- Bruno Bajtela
date: '2018-01-01'
featured: false
publication_types:
- '7'
publishDate: '2018-01-01'
title: Entwurf und Entwicklung der Mandantenfähigkeit von Software-as-a-Service-Architekturen
  am Fallbeispiel einer Enterprise Java-Applikation in der Betriebsphase
url_pdf: ''
---