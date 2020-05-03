---
abstract: Many private and governmental e-health projects are currently developed
  to increase efficiency and quality of health care. As a result sensitive health
  related data is processed and stored for large amounts of patients. This poses a
  risk for misuse of data. This work analyses security architectures of current e-health
  infrastructures and deduces a reference core architecture. Communication channels
  of this reference infrastructure are examined for potential side channel attacks.
  A side channel is defined as unintentional exposure of internal system information.
  Exemplified side channel attacks targeting the given reference infrastructure are
  developed and characterized based on previously published scientific works. As a
  result, three possible attack scenarios are described. Each of the scenarios violate
  the IT security goal of confidentiality. This work points out the fact that the
  Online Certificate Status Protocol (OCSP), a protocol for retrieving up-to-date
  revocation information for electronic certificates, leaks information about actual
  processes being performed within the infrastructure as well as involved patient
  identities. Within the second scenario a deeper analysis of encrypted communication
  between technical system components of e-health infrastructures is sufficient to
  derive concrete use cases and involved medical practitioners. Side channels used
  to uncover these de- tails are based on communication metadata of network traffic
  like packet size, packet inter arrival time, IP address or other protocol header
  information. This work does not focus on breaking of the strong standardized encryption
  in combination with default protocols like Transport Layer Security (TLS) and Internet
  Protocol Security (IPSec) used by the health infrastructures. The third scenario
  describes how an attacker can learn about the amount of prescriptions or patient
  records of a certain patient by observing communication while browsing the e-health
  infrastructure web portal. Similar to the described scenarios before, communication
  metadata is used to deduce information from TLS encrypted network flows. The usage
  of standard encryption protocols like TLS and IPSec are identified as a main reason
  for side channel vulnerabilities within e-health infrastructures. Those protocols
  were not designed to hide communication per se or provide anonymity to clients.
  In addition to the discussion of the attacks, the final part of this work proposes
  possible counter measures against previously mentioned side channel attacks and
  concludes with proposals for future scientific work to further enhance privacy of
  patients within e-health infrastructures.
authors:
- Uwe Kirchengast
date: '2016-01-01'
featured: false
publication_types:
- '7'
publishDate: '2016-01-01'
title: Spannungsfeld Digitalisierung vs. Datenschutz im Gesundheitswesen - Deanonymisierung
  von Patientendaten durch Anwendung von Seitenkanalangriffen auf die Sicherheitsarchitektur
  von e-Health Infrastrukturen
url_pdf: ''
---