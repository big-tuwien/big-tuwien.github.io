---
abstract: In complex software systems managing millions of members and customers and
  their sensitive data, users should only have limited access to those data depending
  on their role in the system. Attribute-based access control (ABAC) systems provide
  fine-grained access restrictions based on attributes of the customer, employee or
  any related object. An ABAC policy can, for example, de- fine that users are granted
  access to another user&iquest;s account if they are in a parent-child relationship
  and the age attribute of the child object is less than 18. Such policies are usually
  implemented on the application-level. Based on ABAC approaches from literature,
  a concept for storing digital ABAC access policies and algorithms to evaluate and
  enforce those policies were defined. Suitable database mechanisms were reviewed
  and a proof of concept was implemented, consisting of a database model for digital
  ABAC policies, modules to intercept requests to the database, to evaluate policies
  and to enforce them by preventing unauthorized requests. An evaluation of different
  access control and performance metrics was conducted, and the results were compared
  with existing, similar software-based solutions. The proof of concept implementation
  and the evaluation show that it is possible to implement attribute-based access
  control solely on the database-level. Complex access policies, limited only by the
  programming language and expressiveness of the database and by the data available
  to the database, can be implemented. Any client accessing the database will only
  be able to view and modify objects that he or she is authorized for. The performance
  impacts of a database- and an application-based implementation are comparable. In
  addition, the database implementation supports more expressive and elegant policies.
  It also provides better security and limits programming errors by separating business
  logic from access control. Compared to similar database implementations, the implementation
  in this thesis supports advanced features such as negative permissions and conflict
  resolution.
authors:
- Matej Kosco
date: '2016-01-01'
featured: false
publication_types:
- '7'
publishDate: '2016-01-01'
title: Concept and Implementation of Attribute-Based Database Access Control Exemplified
  by an Internationally Used Membership Management System
url_pdf: ''
---