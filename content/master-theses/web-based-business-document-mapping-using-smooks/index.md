---
authors:
- Michal Skackov
categories: []
date: '2020-05-08 15:28:13+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Web-based Business Document Mapping using Smooks
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in September 2013.

Electronic commerce (e-commerce) and especially business-to-business (B2B) exchange of data, information or documents, continues to grow in recent years. One of the major challenges in e-commerce is how to align different standards that have emerged over those years \[1,2\]. Enterprises have to invest substantial financial resources to integrate various heterogeneous systems, in order to communicate within organization systems or among trading partners \[3,4,5\]. Rapid developments in Information and Communication Technologies (ICT) brought new cost-effective opportunities for small and medium-sized enterprises (SMEs) to exchange electronic business documents via the Internet using a wide range of integration tools. The current increasing attention into cloud computing as a way of how to minimize costs and introduce pay-per-use models, proves to be of high relevance for the creation of a cloud-ready tool with future potential \[6\].

The objective of this work is to enable SMEs and non-profit organisations to exchange business documents within B2B e-commerce using free of charge, modern information technologies and systems. In order to minimize investments for infrastructure and application licenses, Web-based solutions accessible as cloud services are proposed. This innovative approach opens new possibilities for addressing common issues with mappings and transformations of business documents. Enabling such a solution should motivate SMEs to start using automated B2B electronic communication.

The SmooKs Data Integration (DI) framework, an engine for processing XML and non XML data, currently does not support direct transformation. Therefore an innovative Web-based visual tool, capable of specifying relationships between two XML documents is designed and implemented. The crucial IT artifact of this work, will be the user interface which enables drag and drop mapping of documents and consecutive transformation using the SmooKs DI framework. Furthermore, the whole solution will be deployed as cloud service using Google App Engine and will be accessible from any standard Web browser. The result of this work is the outline of related work on B2B business document standards, mapping and transformation tools.

This thesis follows the guidelines of the design science research methodology \[7\]. The main parts consist of related work relevant to B2B electronic exchange of structured business documents, their mapping and subsequent transformation. When transforming XML documents it is important to understand the model, and schema, as well as query languages \[8,9\]. Furthermore, an analysis of open source data integration frameworks is conducted, followed by a selection of the SmooKs framework. In order to enable direct transformation using SmooKs for XML and other business document standards, an architectural change of the SmooKs DI framework is proposed.

In the technical part, a user interface (UI) will be created. This is elaborated from an analysis of existing integration tools. The relationship between XML structure and tree structure are described in more detail in \[10\]. And is taken into account for the design of a data model used to map source and target document. The design will be tested via direct transformation of the XML to XML using a template engine and SmooKs hosted as a cloud service. An evaluation of the prototype solution will serve as a proof of utility and form an open issue discussion.

Large enterprises, using customized enterprise resource planning systems (ERP), employ more advanced types of middleware such as enterprise application integration (EAI) or enterprise service bus (ESB) for various types of integration. SMEs, to integrate into B2B, focus on less complicated solutions as data integration (DI) tools or software packages, enabling them to extract, transform and load data (ETL) \[11\]. The market is dominated by commercial products from Informatica, IBM, Microsoft, Oracle, and Pervasive \[12\], but there are multiple open source data integration frameworks available (Talend, CoverETL, SmooKs, Pentaho) \[13\]. Talend is the leader in providing open source data integration frameworks. It uses SmooKs for Electronic Data Interchange (EDI). However, the main difference is the value proposition. SmooKs is a framework for Java programmers, while Talend provides a visual tool for non-programmers.

Using a visual tool to specify mapping of source and destination is not new, in fact it goes back as far as the first heterogeneous systems \[14\]. To be more specific, federated database systems (FDBS) managing distributed, autonomous and different databases, laid the cornerstone for a reference architecture of mapping and transformation back in 1980’s \[15\]. Recent classification as well as analysis of mapping tools for data exchange is highlighting that no tool performs well in all mapping situations \[16\]. Most of the current market leaders are using integrated development environment (IDE) software applications installed locally on the desktop.

The implementation of the Web-based editor for mapping models for the data integration framework SmooKs relates to a wide range of technologies. The jQuery framework, a library for JavaScript, is used for the user interface. The transformation works with help of FreeMarker, a template engine, and uses XML related technologies to generate and produce XML, based on a given schema. The entire solution is hosted as a free-of-charge cloud computing service of a Google App engine using Java. In version 1.4 of SmooKs, automatic transformation for UN/EDIFACT was introduced, thus forming solid foundations for support of ANSI X.12, HL7 and other EDI-based data formats. Strong support for various formats (XML, CSV, Fix Width, EDI, Java, JSON, YAML, etc.) and integration with Apache Camel combined with EDI support make SmooKs a strong business document transformation tool used in several other open source products (JBoss ESB, Talend, Mule ESB, WS02).

A literature survey reveals an increased interest into XML-based architecture in Web services \[8,17\]. Due to the simplicity of XML compared to SGML (Standard Generalized Markup Language), XML has an important role in the exchange of various kinds of data, in mapping and transformation \[8,16,18,19\]. Some authors proposed XML to XML transformation using query languages \[15,16\]. The FreeMarker Template Language (FTL) offers a lightweight alternative to common query languages such as XSLT or XQuery. The SmooKs DI framework in conjunction with FreeMarker can be used to perform XML to XML transformation. Furthermore, SmooKs can extract data from EDI messages or read and write data formats other than XML. Further work is required to explore matching meta-models to automate mapping \[20\] with help of semantic systems and implement adapters to plug-in other business document standards.

The master’s programme in Software Engineering &amp; Internet Computing deals with all aspects of distributed heterogeneous software systems, their communication services and standards, and integration into global information networks. This master’s thesis covers areas ranging from Internet technologies, cloud computing or business document standards and their integration into information systems, through innovative design and implementation of the developed prototype. The work outlines relevant technological principles of B2B document mapping and transformation, based on the research and knowledge acquired throughout the study.

\[1\] Philipp Liegl, Business Documents for Inter-Organizational Business Processes, PhD thesis, Technische Universität Wien, Fakultät für Informatik, 2009.

\[2\] Patrick Ziegler and Klaus R. Dittrich, Three Decades of Data Integration – All Problems Solved?, University of Zurich, Zurich, 2004.

\[3\] MulesoftTM, Increasing E-commerce agility. The role of integration in staying ahead of the curve in a changing e-commerce environment, 2010.

\[4\] Christoph Koch, Data Integration Against Multiple Evolving Autonomous Schemata, Universität Wien, Institut fuer medizinische Kybernetik and Artificial Intelligence, 2001.

\[5\] Christian Zehetmeyer, The Diversity and Penetration of EDI in Austria, An Empirical Analysis, Master thesis, Technische Universität Wien, Fakultät für Informatik, 2011.

\[6\] Jeaha Yang, Rangachari Anand, Stacy Hobson, Juhnyoung Lee, Yuan Wang and Jing Min Xu, Data Service Portal for Application Integration in Cloud Computing, IBM TJ Watson Research Center, New York and IBM China Research Laboratory, Beijing, 2011.

\[7\] Alan R. Hevner, Salvatore T. March, Jinsoo Park, Sudha Ram, Design Science in Information Systems Research, MIS Quarterly, 2004.

\[8\] Daniel Fötsch and Andreas Speck, XTC – The XML Transformation Coordinator for XML Document Transformation Technologies, Friedrich-Schiller-University Jena, 2006.

\[9\] Nils Klarlund, Thomas Schwentick and Dan Suciu, XML: Model, Schemas, Types, Logics and Queries, AT&amp;T Labs – Research, USA, University of Marburg, Germany,&nbsp;University of Washington, USA, 2003.

\[10\] Akihiko Tozawa, On Binary Tree Logic for XML and Its Satisfiability Test, IBM Research, Tokyo Research Laboratory, 2004.

\[11\] Noel Yuhanna, The Forrester WaveTM: Enterprise ETL, Q1 2012, Report, 2012.

\[12\] Philip Howard, Comparative costs and uses of Data Integration Platforms, Research and Survey results, 2010.

\[13\] Petr Uher, CoverETL vs. Talend, Pentaho, Clover ETL, Whitepaper, 2009.

\[14\] SoftwareAG, Process Excellence for Digital Enterprise, Annual Report, 2010.

\[15\] Amit P. Sheth, James A. Larson, Federated Database Systems for Managing Distributed, Heterogeneous, and Autonomous Databases, ACM Computing Surveys, 1990.

\[16\] Frank Legler, Felix Naumann, A&nbsp;Classification of Schema Mappings and Analysis of Mapping Tools, 12. GI-Fachtagung fuer Datenbanksysteme in Business, Technologie und Web (BTW 2007), 2007.

\[17\] Dongwon Lee, Query Relaxation for XML Model, University of California, Los Angeles. 2002.

\[18\] Ravi Mani, Joerg Meyer, Pratibha Jamdagneya Sharma, Hovey Raymond Strong,&nbsp;Jr., Tree Construction for XML to XML Transformation, Patent No.: US 7,062,708 B2, 2006.

\[19\] Tom Mens and Pieter Van Gorp, Taxonomy of Model Transformation, Electronic Notes in Theoretical Computer Science 152, Elsevier, 2006.

\[20\] Gerti Kappel, Hosrt Kargl, Gerhard Kramler, Andrea Schauerhuber, Martina Seidl, Michael Strommer and Manual Wimmer, Matching Metamodels with Semantic Systems – An Experience Report, Vienna University of Technology, Verlag Mainz, 2007.

&nbsp;

*Advised by {{% mention "philipp-liegl" %}}, {{% mention "christian-huemer" %}}*