---
abstract: Multiple teams working on a single system may each have different viewpoints,
  and thus, use different models. These models may have partly shared, unique, or
  interrelated information, requiring model integration. To work faster and in a more
  parallel way, temporary inconsistencies between multiple models may be accepted.
  However, shared information only edited by a single team could still be immediately
  made known globally. The two main approaches to model integration are model virtualization,
  i.e., deriving all models from a single source of truth and model synchronization,
  i.e., propagating changes between different materialized models. While model virtualization
  does not allow temporary inconsistencies between models, model synchronization may
  require storing duplicate information redundantly, even if only a single team is
  involved. Thus, this thesis combines model virtualization with model synchronization
  into a hybrid approach. A new model virtualization approach helps arbitrarily adding
  or subtracting models from a base model. The base model can be a single model, an
  intersection or union of multiple models, a modification of another base model,
  or a model derivation. As we can store arbitrary (user) changes to the base model
  without affecting it, we allow temporary inconsistencies and arbitrary changes to
  the base model, e.g., as a result of changing the derivation´s source model. Incompatible
  changes never require user intervention, but just cause semantic constraint violations
  in a newly defined synchronization model, which is valid if and only if all inter-model
  constraints including features derivations are fulfilled. To produce quickfix suggestions
  in (textual) model editors, optimal model synchronization is regarded as finding
  an optimal synchronization model. For this optimization, both model finders and
  heuristic search is employed. Model derivations can be specified using a new basic
  model derivation language, which includes both derivation and synchronization constraints
  in a single model. This allows for pure derivation by not editing the derived model
  as well as pure synchronization by specifying constraints just for inter-model consistency,
  but not for derivation. This hybrid approach is feasible and can support use cases
  like editing multiple models simultanously using virtualization. Our proposed model
  repair does significantly reduce the number of (synchronization) constraint violations
  and prevent new ones due to improved autocompletion as shown in our evaluation scenarios.
authors:
- Robert Bill
date: '2020-01-01'
featured: false
links:
- name: Publik
  url: https://publik.tuwien.ac.at/showentry.php?ID=288220&lang=2
publication: 'Betreuer/in(nen), Begutachter/in(nen): G. Kappel, M. Wimmer, M. Gogolla,
  A. Vallecillo; Institut für Information Systems Engineering, 2020; Rigorosum: 24.02.2020'
publication_types:
- '7'
publishDate: '2020-01-01'
title: Model Integration by Hybrid Model Virtualization
url_pdf: https://publik.tuwien.ac.at/files/publik_288220.pdf
---