---
abstract: Network Address Translation (NAT) poses an inherent problem to many peer-to-peer
  protocols. If one or more of the hosts which want to communicate are located behind
  a NAT gateway, the hosts outside of this network are not able to address IP packets
  to the hosts inside the network. Methods which are used to work around this problem
  are denoted under the umbrella term NAT traversal techniques. This thesis examines
  the NAT traversal capabilities of common VoIP protocols. At the beginning, network
  technologies, which are used by VoIP protocols, are examined. Afterwards, the design
  of NAT devices is described. The work continues by inspecting VoIP protocols, as
  well as the NAT traversal techniques used within these protocols. A comparative
  survey examines each VoIP protocol for a set of predefined NAT environments. It
  is shown, that state of the art protocols are not able to provide optimal traversal
  capabilities for all types of NAT devices. Some protocols are able to establish
  a connection in all examined cases. However, in some setups, they revert to an inefficient
  relayed connection, instead of using a direct peer-to-peer connection. This causes
  a higher latency and additional bandwidth requirements at the location of the VoIP
  provider. The work concludes by proposing enhancements to existing NAT traversal
  techniques, which allow the traversal of NAT gateways in cases where current techniques
  would fail to establish a direct connection. The first technique uses the NAT-PMP
  protocol in order to explicitly request a binding on the NAT device, while the second
  technique tries to predict the port-number, which the NAT device assigns to a particular
  binding. Both techniques can be implemented as extensions to the Interactive Connectivity
  Establishment (ICE) protocol.
authors:
- Günther Starnberger
date: '2007-01-01'
featured: false
links:
- name: Publik
  url: https://publik.tuwien.ac.at/showentry.php?ID=141706&lang=1
publication_types:
- '7'
publishDate: '2007-01-01'
title: NAT Traversal techniques in VoIP protocols
url_pdf: ''
---