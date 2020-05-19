---
abstract: In this thesis, individual steps of a pipeline for processing of the peripheral
  Computed Tomography Angiography (CTA) datasets are addressed. The peripheral CTA
  datasets are volumetric datasets representing pathologies in vascularity of the
  lower extremities in the human body. These pathologies result from various atherosclerotic
  diseases as e.g. the Peripheral Arterial Occlusive Disease (PAOD) and their early
  and precise diagnostics significantly contributes to planning of a later interventional
  radiology treatment.  The diagnostics is based on visualization of the imaged vascular
  tree, where individual pathologic changes, as plaque, calcifications, stenoses of
  the vessel lumen and occluded parts of the vessels are visible. CTA has evolved
  within the recent years into a robust, accurate and cost effective imaging technique
  for patients with both coronary and arterial diseases. As a result of the CTA scanning,
  a set of 1200-2000 transverse slices is acquired, depicting vessels enhanced by
  means of an intravenously injected contrast medium. The number of slices is high
  and therefore their manual examination is laborious and lengthy. As a remedy, post-processing
  methods were developed to allow faster and more intuitive visualization of the imaged
  vascularity. However, simple visualization by means of the traditional techniques
  as maximum-intensity projection (MIP) or direct volume rendering (DVR) is hampered
  due to the presence of bones in the dataset, which occlude the vessels. Therefore,
  a sequence of operations-the processing pipeline-is needed, leading to generation
  of clinically relevant images which depict unobstructed vessels.  In the first step
  of the pipeline the dataset is segmented and the tissues are classified, to allow
  subsequent vessel identification and bone removal. This is a complex task because
  of high density and spatial variability of the tissues. Traditional image processing
  techniques do not deliver acceptable results and therefore in the thesis we present
  new approaches that introduce additional ´anatomic´ information into the segmentation
  and classification process. We propose a probabilistic atlas which enables modeling
  of spatial and density distributions of vessel and bone tissues in datasets, to
  allow their improved classification. In the atlas construction the non-rigid thin-plate
  spline warping and registration of the datasets are applied, to address the high
  anatomic variability among the patients. The concept of the atlas is further extended
  by means of the watershed transform, to further improve precision of the registration
  procedure. Alternatively, we propose and evaluate a technique for vessel enhancement
  based on Hessian filtering to allow detection and recognition of vessel structures
  without operator supervision.  In the second step a geometric model of the vessel
  tree is constructed to derive information about the vessel centerlines. Here, an
  already available algorithm based on the so-called vessel-tracking, implemented
  by means of optimal path searching, is exploited with improvements to make the geometric
  model more precise.  The third step of the processing pipeline-visualization-requires
  this model, since its results can be significantly influenced by a potential imperfections,
  bringing in clinically misleading images. To address limitations of the vessel visualization
  by means of the existing techniques as MIP, CPR or DVR we propose their generalization
  in form of a focus & context-based concept called VesselGlyph. VesselGlyph enables
  to combine intuitively and systematically various visualization techniques to single
  a image to allow better, more comprehensive and unoccluded view of vessels for the
  diagnostic purposes.  To support the design and development of the proposed segmentation,
  modeling and visualization algorithms and to enable their application in the clinical
  environment, we implemented a set of tools grouped in the AngioVis ToolBox software.
  Within this application, individual steps of the processing pipeline are accomplished.
  The toolbox is complemented with additional utilities constituting together a fully-functional
  medical workstation software which is regularly used to process patient data on
  a daily basis in the clinical environment.
authors:
- Matus Straka
date: '2006-01-01'
featured: false
links:
- name: Publik
  url: https://publik.tuwien.ac.at/showentry.php?ID=140331&lang=2
publication: 'Betreuer/in(nen), Begutachter/in(nen): M. Sramek; Institut für Computergraphik
  und Algorithmen, 2006'
publication_types:
- '7'
publishDate: '2006-01-01'
title: Processing and Visualization of Peripheral CT-Angiography Datasets
url_pdf: http://www.cg.tuwien.ac.at/research/publications/2006/straka-phd-thesis/
---