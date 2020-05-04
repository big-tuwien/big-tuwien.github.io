---
abstract: Model-Driven Engineering (MDE) is getting more and more attention as a viable
  alternative to the traditional code-centric software development paradigm. With
  its progress, several model transformation approaches and languages have been developed
  in the past years. Most of these approaches are metamodel-based and, therefore,
  require knowledge of the abstract syntax of the modeling languages, which in contrast
  is not necessary for defining domain models using the concrete syntax of the respective
  languages.   Based on the by-example paradigm, we propose Model Transformation By-Example
  (MTBE), to cope with shortcomings of current model transformation approaches. Our
  approach allows the user to define semantic correspondences between concrete syntax
  elements with the help of special mapping operators. This is more user-friendly
  than directly specifying model transformation rules and mappings on the metamodel
  level. In general, the user's knowledge about the notation of the modeling language
  and the meaning of mapping operators is sufficient for the definition of model transformations.
  The definition of mapping operators is subject to extension, which has been applied
  for the definition of mapping operators for the structural and the behavioral modeling
  domain. However, to keep things transparent and user-friendly, only a minimal set
  of mapping operators has been implemented. To compensate for the additional expressiveness
  inherent in common model transformation languages we apply reasoning algorithms
  on the models represented in concrete as well as in abstract syntax and on the metamodels
  generating adequate transformation code.  In order to fulfill the requirements for
  a user-friendly application of MTBE, proper tool support and methods to guide the
  mapping and model transformation generation tasks are a must. Hence, a framework
  for MTBE was designed that builds on state-of-the-art MDE tools on the Eclipse platform,
  such as the Eclipse Modeling Framework (EMF), the  Graphical Modeling Framework
  (GMF), the Atlas Transformation Language (ATL), and the Atlas Model Weaver (AMW).
  The decision to base our implementation on top of Eclipse and further Eclipse projects
  was driven by the fact, that there is a huge community we can address with our MTBE
  plug-in.  Finally, we evaluate our approach by means of two case studies covering
  the structural as well as behavioral modeling language domain.
authors:
- Michael Strommer
date: '2008-01-01'
featured: false
links:
- name: Publik
  url: https://publik.tuwien.ac.at/showentry.php?ID=166165&lang=2
publication_types:
- '7'
publishDate: '2008-01-01'
title: Model Transformation By-Example
url_pdf: http://publik.tuwien.ac.at/files/PubDat_166165.pdf
---