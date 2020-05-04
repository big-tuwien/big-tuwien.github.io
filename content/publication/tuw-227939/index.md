---
abstract: The aim of this master thesis is to reduce the conceptual gap between software
  modeling and model checking. While model checking is successfully applied for hardware
  verification, it is not widespreadly used in model-driven engineering (MDE). Thus,
  we tried to reduce this gap by combining modeling and model checking concepts.  This
  thesis first describes the history and basic idea of both MDE and model checking
  with a focus on the technologies used in this thesis. Before presenting our new
  approach, existing solutions are compared. Most approaches propose to extend the
  Object Constraint Language (OCL) by temporal aspects. This allows to describe the
  behavior of a software system additionally to various properties of static models.
  However, one of the main missing features in general seems to be a user-friendly
  representation of the verification result helpful for debugging. Often, the technical
  spaces are changed.  With our solution we provide (i) a temporal OCL extension based
  on the Computational Tree Logic (CTL) and (ii) an OCL extension that introduces
  path selectors to extract interesting system configurations from the state space.
  Both OCL extensions were formally defined and implemented. We describe systems in
  terms of state spaces consisting of EMOF-model states and state transitions containing
  a mapping between model elements of different states. The system behavior is specified
  using an initial Ecore model and graph transformations based on the Henshin tool2.
  The approach, however, is designed to be flexible enough to allow an easy integration
  of any kind of behavior specification as long as a suitable state space can be derived
  thereof. Our model checking framework is developed with a focus on delivering not
  only the results, but also making the system behavior leading to the result comprehensible
  by providing a suitable tool including a web interface.  The implementation was
  evaluated in terms of performance to find out the maximum evaluable model size and
  query complexity. Further, a qualitative user study was conducted for evaluating
  the CTL extension and the tool. The results of this study indicate that both the
  CTL-based extension of OCL as well as the tool are a promising first step to integrate
  model checking in the MDE life cycle.
authors:
- Robert Bill
date: '2014-01-01'
featured: false
links:
- name: Publik
  url: https://publik.tuwien.ac.at/showentry.php?ID=227939&lang=2
publication_types:
- '7'
publishDate: '2014-01-01'
title: Towards Software Model Checking in the Context of Model-Driven Engineering
url_pdf: http://publik.tuwien.ac.at/files/PubDat_227939.pdf
---