---
advisors:
- gertrude-kappel
authors:
- Martin Bernauer
categories: []
date: '2020-05-19 12:38:12+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Maintaining Consistency of Data on the Web
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in December 2004.

Increasingly more data is becoming available on the Web, estimates speaking of 1 billion documents in 2002. Most of the documents are Web pages whose data is considered to be in XML format, expecting it to eventually replace HTML, the current lingua franca of the Web, e.g., by XHTML.

A common problem in designing and maintaining a Web site is that data on a Web page often replicates or derives from other data, the so-called base data, that is usually not contained in the deriving or replicating page. Two properties of Web sites account for this situation. First, the hypertext structure of a Web site not necessarily coincides with the structure of its underlying conceptual domain model, thus it may be necessary to present a single data item on several pages. Second, the content of pre-generated Web pages is often drawn from legacy systems, usually relational databases. In this case Web pages replicate data items from databases.

Consequently, replicas and derivations become inconsistent upon modifying base data in a Web page or a relational database. For example, after modifying a product’s price in the database, already pre-generated Web pages offer the product at an out-dated price. Or, after assigning a thesis to a student and modifying the Web page that describes it in detail, the thesis is still incorrectly contained in the list of offered thesis, missing in the list of ongoing thesis, and missing in the advisor’s teaching record.

The thesis presents a solution by proposing a combined approach that provides for maintaining consistency of data in Web pages that (i) replicate data in relational databases, or (ii) replicate or derive from data in Web pages. Upon modifying base data, the modification is immediately pushed to affected Web pages. There, maintenance is performed incrementally by only modifying the affected part of the page instead of re-generating the whole page from scratch.

The proposed approach provides for consistent, up-to-date Web pages any time. It is efficient by providing incremental page maintenance techniques, generic by maintaining consistency of XML data in general, flexible by reacting to modifications in Web pages of other businesses, transparent by maintaining a business’ autonomy in managing its data, open by allowing future extensions to be built on top of it, and extensible by enabling the integration of arbitrary legacy systems.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Bernauer_M.pdf)