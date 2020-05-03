---
abstract: Multiple teams working on a single system may each have different viewpoints,
  and<br> thus, use different models. These models may have partly shared, unique,
  or interrelated<br> information, requiring model integration. To work faster and
  in a more parallel way,<br> temporary inconsistencies between multiple models may
  be accepted. However, shared<br> information only edited by a single team could
  still be immediately made known globally.<br> The two main approaches to model integration
  are model virtualization, i.e., deriving<br> all models from a single source of
  truth and model synchronization, i.e., propagating<br> changes between different
  materialized models. While model virtualization does not allow<br> temporary inconsistencies
  between models, model synchronization may require storing<br> duplicate information
  redundantly, even if only a single team is involved.<br> Thus, this thesis combines
  model virtualization with model synchronization into a hybrid<br> approach. A new
  model virtualization approach helps arbitrarily adding or subtracting<br> models
  from a base model. The base model can be a single model, an intersection or<br>
  union of multiple models, a modification of another base model, or a model derivation.<br>
  As we can store arbitrary (user) changes to the base model without affecting it,
  we<br> allow temporary inconsistencies and arbitrary changes to the base model,
  e.g., as a<br> result of changing the derivation´s source model. Incompatible changes
  never require<br> user intervention, but just cause semantic constraint violations
  in a newly defined<br> synchronization model, which is valid if and only if all
  inter-model constraints including<br> features derivations are fulfilled. To produce
  quickfix suggestions in (textual) model<br> editors, optimal model synchronization
  is regarded as finding an optimal synchronization<br> model. For this optimization,
  both model finders and heuristic search is employed.<br> Model derivations can be
  specified using a new basic model derivation language, which<br> includes both derivation
  and synchronization constraints in a single model. This allows<br> for pure derivation
  by not editing the derived model as well as pure synchronization by<br> specifying
  constraints just for inter-model consistency, but not for derivation.<br> This hybrid
  approach is feasible and can support use cases like editing multiple models<br>
  simultanously using virtualization. Our proposed model repair does significantly
  reduce<br> the number of (synchronization) constraint violations and prevent new
  ones due to<br> improved autocompletion as shown in our evaluation scenarios.
authors:
- Robert Bill
date: '2020-01-01'
featured: false
publication: '*Model Integration by Hybrid Model Virtualization*'
publication_types:
- '7'
publishDate: '2020-01-01'
url_pdf: https://publik.tuwien.ac.at/files/publik_288220.pdf
---