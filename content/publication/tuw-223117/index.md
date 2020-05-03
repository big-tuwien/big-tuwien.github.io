---
abstract: Accounting Information Systems (AIS) are essential for companies not only
  to record and track what events are happening or what events have happened in the
  past, they are also one of the most important tools for management to predict the
  financial future of a firm and take according actions. To enable an AIS to precisely
  record economic data and apply reasoning on them, it is crucial that the data structure
  of an AIS is built upon the economic phenomenas of a company´s business. Accordingly,
  it is already important to have a detailed understanding of the company´s economic
  actions at the design time of an AIS.<br> <br> Like in most software development
  projects, the dilemma during design time of an IT product is the language barrier
  between the domain expert, providing vital input for defining the requirements,
  and the IT professional, designing and developing the IT product. In most cases
  the domain expert is not capable of understanding IT specific terms, and the IT
  professional is not capable of completely understanding the specific area of the
  domain expert. Nevertheless, to successfully complete an IT product, these two groups
  still need to unambiguously communicate with each other by using a common language.<br>
  <br> When designing an AIS, the domain at hand is the accounting/business domain.
  Thus, a business modeling language describing economic phenomenas of a company can
  be used as such a common language to define requirements. One powerful business
  modeling language today is the Resource-Event-Agent ontology (REA). It not only
  allows describing events of the present and the past, it also allows specification
  of commitments made for future events. Consequently, it perfectly fits our requirement
  to capture the economic phenomenas of an AIS. However, REA is somewhat vague in
  the definition of its concepts and the current representation is merely IT related,
  which makes it hard to be understood by business experts. Accordingly, REA still
  cannot be used as a common communication language for the AIS design phase.<br>
  <br> Given these limitations, in this thesis we have taken upon the challenge to
  develop an unambiguous and intuitive graphical domain-specific representation for
  the REA ontology called the REA-DSL. First, we formalize the REA ontology by providing
  a REA-DSL meta-model incorporating the REA concepts resources, events, agents, commitments,
  and types as well as concepts known from database modeling. Subsequently, we create
  a graphical notation for the REA-DSL using different shapes for different REA concepts.
  Additionally, to reduce the complexity of the models, we split the REA-DSL into
  five interlinked views. A serialization format for the REA-DSL is provided by the
  REA-XML language. Furthermore, we specify a mapping between the conceptual REA-DSL
  and a database description language. This enables the semi-automatic generation
  of database structures for an AIS.<br> <br> The presented REA-DSL serves as an unambiguous
  and powerful business modeling language which can be used by IT and business experts
  for faster designing a robust AIS.
authors:
- Dieter Mayrhofer
date: '2012-01-01'
featured: false
publication: '*REA-DSL: Business Model Driven Data Engineering*'
publication_types:
- '7'
publishDate: '2012-01-01'
url_pdf: http://publik.tuwien.ac.at/files/PubDat_223117.pdf
---