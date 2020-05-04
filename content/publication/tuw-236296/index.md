---
abstract: 'A distributed system executes one program or algorithm on multiple networked
  nodes. As computer network systems continue growing, it becomes increasingly complex
  to maintain their robustness. Some of the issues that have to be dealt with in a
  network are: subverted systems following an adversarial attack, unreliable transmission
  of data, as well as hardware failures. The Byzantine fault model encompasses all
  possible faults in a system, which, among others, include crash, timing, and omission
  failures. Continuous discoveries of new technologies make it imperative that fault
  tolerance is addressed properly in mission-critical systems. We present a system
  that provides functionality for testing and benchmarking on a distributed system.
  This framework offers a common ground to be able to make a fair performance comparison
  of distributed fault-tolerant protocols. The framework´s practicality is of primary
  concern. This means that it should be easily deployed, run, and maintained. Its
  modular design allows the code baseline to be extended and configured with ease.
  Moreover, the documentation of the framework, which includes comprehensive code
  documentation, as well as visual representations such as class diagrams, facilitate
  an easier understanding at both a lower and higher level. Implementing the framework
  in Java allows for cross-platform deployment and execution, as well as an object-oriented
  design, which eases modularity. Having a modular framework to test distributed algorithms
  enables the use of novel ideas for storage networks, such as network coding, for
  Byzantine fault-tolerant algorithms. Network coding is a way to improve a network´s
  efficiency and resilience to attacks, and poses an alternative methodology to provide
  Byzantine fault tolerance compared to those solely relying on cryptography. Coding
  essentially breaks up data into smaller packets or combines data packets into the
  original form. Although the current state of the framework does not provide a coding
  algorithm, the default fault-tolerant protocol implementation integrates the calls
  to an abstract coding scheme to encode and decode data. Extending the framework
  with a coding scheme, such as Reed-Solomon, would enable the full use of this functionality.'
authors:
- Adrian Djokic
date: '2014-01-01'
featured: false
links:
- name: Publik
  url: https://publik.tuwien.ac.at/showentry.php?ID=236296&lang=2
publication_types:
- '7'
publishDate: '2014-01-01'
title: Practical framework for Byzantine fault-tolerant systems
url_pdf: ''
---