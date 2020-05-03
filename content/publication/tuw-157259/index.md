---
abstract: 'Building Models or Building Information Modells (BIM) are fine-grained,
  multi-faceted, integrated computational models of physical buildings. They capture
  not only the geometric, but also semantic data of building components and their
  relations. The promise of building information models is to support the entire lifecycle
  of a building, from concepzion through operation and maintenance to decommisioning.
  Building models servers are software systems that maintain such models and provide
  access to local and remote client appliciations.  Existing software architectures
  for building model servers are strongly focused on the requirements of the design
  phase and, to a lesser extent, the construction phase of the building lifecycle.
  These requirements resemble those of source code version control systems, with infrequent
  but potentially massive check-in/check-out operations on a central model repository.
  The subject of this dissertation is the design of building model servers suitable
  for support of the operation phase of a building. The prototypical application used
  here is simulation-based ligthing control, which requires a fine-grained and up-to-date-model
  of the controlled space and devices, mcuh more so than typical facility management
  applications. The model is therefore connected to sensors and actuators within the
  building, keeping itself updated with sensor data and also acting as an interface
  to building systems for client applications. The main challenge for such operation-phase
  building models are 1.) the integration of a wide range of different data sources
  and endpoints, and 2.) the efficient handling of sustained rates of incoming data
  while ensuring simple, uninterrupted, low-latency access to model data. Certain
  client applications (such as lighting control) even have soft real-time requirements.
  Great emphasis must therefore be placed on performance, scalability, as well as
  modifiability. This dissertation argues that existing model server architectures
  are not suitable to ensure these quality attributes, particularly because they are
  not designed for high concurrency. At the core of the proposed architectrue, the
  building obejct model is implemented in a bitemporal main meomry database with persistent
  backing storage. Changes to model obejcts are versioned, allowing simple and transparent
  access to a full model history ("time travel"). The database ensures serializable
  transactions with a high degree of concurrency using a variant of the multi-version
  transaction ordering (MVTO) algorithm. Transactions amay be prioritised to ensure
  low latency updates. The performance and scalability of the concurrency control
  mechanism compares favourably with a simple locking scheme. The model server provides
  full support for happened-before and known-before ordering of date even when the
  data arrive unordered or very late by allowing retroactive insertion of records.
  Distribution design is one of the key points in the software architecture: instead
  of using a reference architecture (such as client-server) and working around its
  limitations, the moste beneficial runtime locations of tasks and data for given
  requirements are considered. This is particularly important for client appliciations.
  Two classes of client component behaviour are identified. Interactive behaviour
  is characterised by bursts of short read/write accesses to a varying set of model
  objects, possibly in reaction to model changes. Interactive components require little
  CPU and memory, but call for low-latency model access and immediate notification
  od model changes. They access the model as agents that are executed as threads within
  the model service, following the principle to run code where its data are. Agents
  can be installed and activated at run-time without service disruption. Batch behaviour
  is characterised by intensive, long-running work on a fixed set of model objects,
  as is typical for building simulation and other analysis tasks. Write operations
  are rare. Such tasks call for great amounts of CPU cycles and are typically less
  affected by concurrent model changes. Batch components are therefore distributed
  to other systems and work on snapshot copies of the required model subset. Combined
  with a space-based communication layer, this distribution is transparent to a high
  degree and allows simple load distribution with a minimum of central administration.
  Communication with the building systems is performed through an external message-queue
  infrastructure. The model service uses a flexible processing pipeline served by
  thread pools to locate and update the target obejcts corresponding to incoming messages.
  For concurrency-optimised internal communications (e.g. between agents), the model
  service provides a simple generalised message queuing system that can transparently
  connect to the external messaging system if needed. A facility for runtime-pliggable
  code is provided to achieve a hiogh degree of modifiability and availability.'
authors:
- Klaus A. Brunner
date: '2007-01-01'
featured: false
publication_types:
- '7'
publishDate: '2007-01-01'
title: The Design of a Building Model Service
url_pdf: ''
---