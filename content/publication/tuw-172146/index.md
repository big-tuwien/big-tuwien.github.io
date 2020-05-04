---
abstract: 'Traceability in software development is often seen as bureaucratic burden
  rather than an opportunity for efficiency improvements. Consequently, small development
  teams are hardly motivated to embrace the concept and make information flow and
  decision making in their projects traceable. This thesis aims to present a viable
  solution for linking intermediate products (artefacts) of the project - a method
  of integrating tools used in the development process - so that small development
  teams can reap the benefits of traceability with a reasonable amount of effort.
  The primary issue is the fact that there are various tools available and in use
  - a common standard of communication is needed to enable information exchange between
  any pair or set of tools. The proposal of this thesis an XML-based message format
  - messages containing information to identify artefacts, and messages defining relationships
  between pairs of artefacts. Using messages instead of interfaces allows for looser
  coupling, enabling integration of a tool without adapting its underlying concepts.
  It is therefore possible to achieve quick results by extending one tool to send
  messages about its artefacts, and another tool to process these messages and offer
  its users the information obtained from them - the first step towards traceability.
  Using XML as base format allows easy message validation against an XML schema and
  also offers extensibility to incorporate additional information for tighter tool
  integration where this is desired. As proof of concept, two standalone tool prototypes
  have been developed and then extended to communicate via the suggested message format:
  a requirements management and a test tracking tool. The set-up shows that traceability
  links can be established across tool borders and that this provides benefits to
  the users. With the shared information, for example reports on test coverage or
  test results of specific requirements are possible.'
authors:
- Martin Schwarzbauer
date: '2008-01-01'
featured: false
links:
- name: Publik
  url: https://publik.tuwien.ac.at/showentry.php?ID=172146&lang=2
publication_types:
- '7'
publishDate: '2008-01-01'
title: Design and development of a traceability framework for small software development
  teams - a message-oriented approach
url_pdf: ''
---