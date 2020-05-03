---
abstract: In this thesis a thorough description of UN/CEFACT´s Modeling Methodology
  (UMM) was given. We started with identifying problems and needs in real-world B2B
  scenarios. Based on these needs we depicted the requirements for a methodology like
  UMM in order to denote cross-enterprise business processes. Participating in such
  an inter-organizational process requires a partner to agree on a certain choreography.
  Furthermore, a participant must provide compliant interfaces to his information
  systems according to the agreed choreography. However, if each participant describes
  the same process just from its own view, the resulting process descriptions won´t
  match. Thus, we require an approach - like UMM - in order to specify process from
  a global point of view. <br> Moreover, we depicted the need for an adequate tool
  support in order to endorse modelers in producing UMM compliant models. Afterwards,
  we presented some technical details in respect to our implementation called UMM
  Add-In. The UMM Add-In in an extension to the UML tool Enterprise Architect written
  in .NET. <br> After giving some general information about UMM´s history and the
  responsible standardization body - the United Nations Centre for Trade Facilitation
  and Electronic Business (UN/CEFACT) - we introduced worksheets and their role in
  UMM to capture requirements. In addition, we described the integration of a worksheet
  editor into the UMM Add-In as well as the benefits thereof. <br> The next chapter
  comprises a guide supporting the creation of a UMM compliant model based on the
  know-how gathered by worksheets. The guide explains step by step the modeling of
  each view in the UMM. Furthermore, the required steps to draw up a UMM model are
  illustrated using an example about an ordering process.<br> However, giving only
  a guide for modeling UMM might result in models, which are not compliant to the
  UMM meta model defined by the UML profile for UMM. This is not a modeler´s failure,
  but a presumable result when applying a formal notation like UMM without a computational
  verification. Hence, we illustrated the need for validating UMM models and gave
  an introduction into the UML profile for UMM. Furthermore, we presented the implementation
  of a validation engine as part of the UMM Add-In based on the constraints defined
  in the UML profile for UMM.<br> In a service-oriented architecture, XML-based process
  descriptions are utilized to configure information systems according to a particular
  process. In our case, we have already modeled collaborative processes by means of
  UMM. It follows, that an automatic generation of process descriptions is required
  in order to support the deployment of B2B information systems. In the UMM Add-In
  we implemented a transformation engine for generating BPEL compliant artifacts.
  BPEL seems to be the winner amongst the set of lately emerged choreography languages.
  <br> Modeling exchanged business information and deriving document schemes thereof
  is the last building block to gain a complete set of artifacts that together describe
  a collaborative process. Describing the derivation of schemes as well as a reference
  implementation thereof according to rules standardized by UN/CEFACT is subject to
  the following chapter. <br> Finally, in the appendix we included the UML profile
  for UMM, denoting the UMM meta model. During the writings of our thesis we attended
  the UN/CEFACT conferences and participated a lot in the development of this profile.
  <br> However, we think that with our thesis a cornerstone has been laid, which allows
  the development of additional features. This might include the development of a
  registry connector in order to support the registration and retrieval of business
  collaboration models or parts thereof. In addition, features like the generation
  of BPEL artifacts or document schemes require some improvements in order to be ready
  for use in production environments. <br> We hope, that the UMM Add-In and this thesis
  will help to increase the diffusion of UMM within the business process modeling
  world. Furthermore, our work should be a step forward to achieve the transition
  from a data-centric business modeling to a process-centric business modeling.
authors:
- Philipp Liegl
- Rainer Schuster
- Marco Zapletal
date: '2006-01-01'
featured: false
publication: '*A UML Profile and Add-In for UN/CEFACT''s Modeling Methodology*'
publication_types:
- '7'
publishDate: '2006-01-01'
url_pdf: http://publik.tuwien.ac.at/files/pub-inf_3605.pdf
---