---
abstract: Activity auditing is the practice of recording activities on a system and
  later analysing them regarding abuse of the system or for unauthorized activity.
  Being able to audit a system is also necessary to comply with certain regulations
  and certifications that restrict system and information usage. An auditor can use
  the audit log data to verify that the organisation´s systems, and the information
  that is stored on them, were used in accordance with the requirements of the relevant
  regulations. By proving such compliance, auditing not only allows detection of abuse,
  but also allows the organisation to prove their accountability by showing that they
  adhere to strict standards. An example where auditing system usage is useful can
  be found in exercise environments at universities. Various security courses provide
  exercises where students can try security related tasks on (virtual) machines and
  experiment with security tools in a controlled environment. Students reach this
  environment from the internet by using Secure Shell (SSH). This environment may
  deliberately contain vulnerable services or software for teaching purposes, but
  students are not allowed to misuse the environment by attacking it or other hosts
  on the internet. The purpose of this thesis is to develop an activity auditing concept
  that allows the course administration to track abuse of the environment back to
  an attacker. To achieve this goal, in this thesis expert interviews are used, threat
  modelling techniques and risk management methods to determine the requirements for
  an activity auditing solution. Further, a literature review is performed to supplement
  the requirements profile. The identified requirements profile is compared with published
  solutions and, based on the obtained overall picture, an adequate solution concept
  is created. This concept is then implemented as a proof of concept implementation.
  The implementation is evaluated and tested to show that the identified requirements
  are fulfilled. A central element of the concept is the recording of all activities
  without exception by logging all in- and output data that is being transfered via
  Secure Shell (SSH). The concept records all student activity by recording all in-
  and output data sent over the encrypted SSH connection. The resulting activity audit
  logs can then be forensically examined and they can be replayed for additional insights.
  Finally, the work shows if and to what extent the solution concept is fit for use
  in different environments.
authors:
- Florian Pritz
date: '2019-01-01'
featured: false
publication_types:
- '7'
publishDate: '2019-01-01'
title: Shell Activity Logging and Auditing in Exercise Environments of Security Lectures
  using OSS
url_pdf: ''
---