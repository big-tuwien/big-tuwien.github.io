---
authors:
- Elke Michlmayr
categories: []
date: '2020-05-08 18:02:38+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Ant Algorithms for Self-Organization in Social Networks
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in May 2007.

Peer-to-peer networks and folksonomies are like living organisms, ever growing and changing as time goes on. This thesis addresses the applicability of algorithms derived from the self-organizing and emergent behavior observed from ant colonies to these complex networks for two specific purposes, namely (1) content-based search in unstructured peer-to- peer networks, and (2) the extraction of adaptive user profiles from folksonomies.

For search in unstructured peer-to-peer networks, the main goal is to find the shortest path from every querying peer to one or more answering peers that possess resources which are appropriate answers for the given query. The S EM A NT algorithm, which is designed for this task, is based on reputation learning. In reputation learning, the information about the remote peers’ resources is gained passively by observing the user queries and their answers that are forwarded through the local peer. Every successful query evokes small updates in the routing tables of those peers that are included in the path between the querying and the answering peer. The routing tables are used for subsequent queries to decide which link to follow in order to find appropriate resources. The S EM A NT algorithm is compliant with the Ant Colony Optimization meta-heuristic, and it employs a probabilistic procedure to select outgoing links for query forwarding. This procedure combines an exploiting strategy, which selects those links currently known as the most appropriate ones, with an exploring strategy, which also follows links not currently known as the best ones with the aim of finding better paths not yet explored. A weight defines the ratio between the strategies.

Since the S EM A NT algorithm is a content-based approach to peer-to-peer search, its performance depends on how the content is distributed in the network. The evaluation of the algorithm includes an investigation to which extent this is the case. Based on these results, we develop strategies for improvement. Under the assumption that the resources in the network are annotated according to a taxonomy, and that the query vocabulary is restricted to the leaf topics from the same taxonomy, it is possible to consider also the upper-level topics in the query routing procedure of the algorithm in order to increase its performance.

Ant algorithms include an evaporation feature for integrating a time factor when incrementally creating solutions. This feature is beneficial for the task of learning adaptive user profiles from tagging data. For this purpose we design the Add-A-Tag algorithm, which is based on a combination of an evaporation feature for adapting the user profile to trends over time, and the co-occurrence technique for determining the relationships between tags. The user profiles created with the Add-A-Tag algorithm are semantic networks derived from the structure of the tagging data, and they are adaptive in the sense that they change according to changes in a user’s tagging behavior. In addition to the long-term interests of a user, also his or her short-term interests are included in the profile at any given point of time. We present a tool for visualizing the changes in the profile over time, and we show how to exploit the profile for personalized browsing of annotated data sources.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Michlmayr_E.pdf)

*Advised by {{% mention "gertrude-kappel" %}}*