---
abstract: The Web Services Transaction protocol family includes the WS-AtomicTransaction
  and the WSBusinessActivity specifications in order to carry out distributed transactions
  in a Web Services (WS) environment. The WS-AtomicTransaction specification defines
  all necessary interfaces to carry out transactional work. In contrary, the WS-BusinessActivity
  specification for long-running transactions intentionally left the interface between
  initiator and coordinator undefined. This allows vendors to integrate WS-BusinessActivity
  coordinators into their business process engines. However, it requires proprietary
  protocols between initiator and coordinator. We propose an extension protocol to
  the WS-BusinessActivity specification that explicitly defines this interface between
  initiator and coordinator. This extension allows coordinators and initiators from
  different vendors to interoperate transparently. Accordingly, participants no longer
  need to trust an initiator-selected and likely initiator-run coordination service,
  but may use commonly trusted, third-party coordination services.
authors:
- Hannes Erven
- Georg Hicker
- Christian Huemer
- Marco Zapletal
date: '2007-07-09'
featured: false
links:
- name: Publik
  url: https://publik.tuwien.ac.at/showentry.php?ID=141391&lang=2
publication: 'Talk: 2007 IEEE International Conference on Web Services (ICWS 2007),
  Salt Lake City, Utah, USA; 07-09-2007 - 07-13-2007; in: "2007 IEEE International
  Conference on Web Services (ICWS 2007)", IEEE Computer Society, Los Alamitos, CA,
  USA (2007), ISBN: 0-7695-2924-0; 216 - 224'
publication_types:
- '1'
publishDate: '2007-07-09'
title: 'The Web Services-BusinessActivity-Initiator (WS-BA-I) Protocol: an Extension
  to the Web Services-BusinessActivity Specification'
url_pdf: http://publik.tuwien.ac.at/files/pub-inf_5006.pdf
---