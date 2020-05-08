---
authors:
- Wolfgang Hoschek
categories: []
date: '2020-05-08 15:45:02+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: A Univied Peer-to-Peer Database Framework for XQueries over Dynamic Distributed
  Content and its Application for Scalable Service Discovery
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in March 2002.

In a large distributed system spanning administrative domains such as a Grid, it is desirable to maintain and query dynamic and timely information about active participants such as services, resources and user communities. The web services vision promises that programs are made more flexible and powerful by querying Internet databases (registries) at runtime in order to discover information and network attached third-party building blocks. Services can advertise themselves and related metadata via such databases, enabling the assembly of distributed higher-level components. In support of this vision, this thesis shows how to support expressive general-purpose queries over a view that integrates autonomous dynamic database nodes from a wide range of distributed system topologies.

We motivate and justify the assertion that realistic ubiquitous service and resource discovery requires a rich general-purpose query language such as XQuery or SQL. Next, we introduce the Web Service Discovery Architecture (WSDA), which subsumes an array of dis- parate concepts, interfaces and protocols under a single semi-transparent umbrella. WSDA specifies a small set of orthogonal multi-purpose communication primitives (building blocks) for discovery. These primitives cover service identification, service description retrieval, data publication as well as minimal and powerful query support. The individual primitives can be combined and plugged together by specific clients and services to yield a wide range of be- haviors and emerging synergies. Based on WSDA, we introduce the hyper registry, which is a centralized database node for discovery of dynamic distributed content, supporting XQueries over a tuple set from an XML data model. We address the problem of maintaining dynamic and timely information populated from a large variety of unreliable, frequently changing, autonomous and heterogeneous remote data sources.

However, in a large cross-organizational system, the set of information tuples is partitioned over many such distributed nodes, for reasons including autonomy, scalability, availability, performance and security. This suggests the use of Peer-to-Peer (P2P) query technology. Consequently, we take the first steps towards unifying the fields of database management systems and P2P computing. As a result, we propose the WSDA based Unified Peer-to-Peer Database Framework (UPDF) and its associated Peer Database Protocol (PDP), which are unified in the sense that they allow to express specific applications for a wide range of data types (typed or untyped XML, any MIME type), node topologies (e.g. ring, tree, graph), query languages (e.g. XQuery, SQL), query response modes (e.g. Routed, Direct and Referral Response), neighbor selection policies, pipelining, timeout and other scope characteristics.

The uniformity and wide applicability of our approach is distinguished from related work, which (1) addresses some but not all problems, and (2) does not propose a unified framework.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Hoschek_W.pdf)

*Advised by {{% mention "gertrude-kappel" %}}*