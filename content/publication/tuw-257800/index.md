---
abstract: Storage systems represent a key component in a modern data center architecture.
  Because of its central role, the storage system design shapes the structure of the
  whole data center and, therefore, also impacts the overall infrastructure costs
  to a large extent. Since almost every business application needs to store information
  in some way, the underlying storage technologies must be capable of processing large
  amounts of data in a reliable and highly performant way. Due to the virtualization
  and cloud computing paradigm shift, business applications switch from physical servers
  to virtual machines that are hosted by large clusters of hypervisors or even completely
  transparently in a cloud computing infrastructure. As a result, the physical location
  of the data moves from the disk drives of a single application server to a large-scale
  storage system that provides a reliable data storage service over the network to
  a multitude of clients. Alongside traditional Storage Area Networks (SANs), a number
  of alternative storage architectures have emerged that instead of relying on proprietary
  hardware components use open-source software to build a cluster of a large number
  of intelligent storage nodes. In order to fulfill the demands for data availability,
  a distributed storage system needs to maintain multiple real-time copies of a given
  data set. For this purpose, instant data replication is commonly used as a mechanism
  to achieve data consistency among a set of replicas. Although several architectural
  design approaches exist to construct such a cluster, each one impacts user-visible
  aspects like performance, data availability and scalability in a different manner.
  However, due to the specific requirements, not all distributed storage architectures
  are suitable to serve as back end in a large-scale virtualization environment. This
  thesis analyzes different methods of building a distributed storage cluster out
  of open-source components. Moreover, it highlights the characteristics of various
  system architectures and verifies their compliance with the general requirements
  for resilient distributed services. Furthermore, the architectural analysis is combined
  with the practical evaluation of two open-source case studies. In a realistic use
  case scenario, those case studies are tested regarding system performance and fault
  tolerance behavior in order to reveal their architectural strengths and weaknesses.
  The results of the practical evaluation refine the outcome of the analysis, which
  aims to identify design-related aspects that directly impact the performance capabilities
  or the data availability of a distributed storage system. Finally, the insight obtained
  from this research regarding different distributed system architectures is applicable
  as a guideline for planning the storage back end for a large-scale enterprise virtualization
  environment using open-source software.
authors:
- David Riepl
date: '2016-01-01'
featured: false
links:
- name: Publik
  url: https://publik.tuwien.ac.at/showentry.php?ID=257800&lang=2
publication_types:
- '7'
publishDate: '2016-01-01'
title: Analysis of Scalable Open-source Distributed Storage Systems with an Emphasis
  on Data Availability and Performance
url_pdf: ''
---