---
authors:
- Andreas Mehlführer
categories: []
date: '2020-05-08 15:44:51+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: 'Web Scraping: A Tool Evaluation'
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in March 2009.

The WWW grows to one of the most important communication and information medium. Companies can use the Internet for various tasks. One possible application area is the information acquisition. As the Internet provides such a huge amount of information it is necessary to distinguish between relevant and irrelevant data. Web scrapers can be used to gather defined content from the Internet. A lot of scrapers and crawlers are available. Hence we decided to accomplish a case study with a company. We analyze available programs which are applicable in this domain.

The company is the leading provider of online gaming entertainment. They offer sports betting, poker, casino games, soft games and skill games. For the sports betting platform they use data about events (fixtures/results) which are partly supplied by extern feed providers. Accordingly, there is a dependency on providers. Another problem is that smaller sports and minor leagues are not covered by the providers. This approach requires cross checks which are manual checks with websites if provider data differs and the definition of a primary source (source which is used in case of different data from providers) have to be done by data input user. Data about fixtures and results should be delivered by a company owned application.

This application should be a domain-specific web crawler. It gathers information from well defined sources. This means bwin will not depend on other providers and they can cover more leagues. The coverage of the data feed integration tool will increase. Furthermore, it eliminates the cross checks between different sources. The first aim of this master thesis is to compose a functional specification for the usage of robots to gather event data via Internet and integrate the gathered information into the existing systems. Eight selected web scrapers will be evaluated and checked based on a benchmark catalogue which is created according to the functional specification. The catalogue and the selection are conceived to be reused for further projects of the company. The evaluation should result in a recommendation which web scraper fits best the requirements of the given domain.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Mehlführer_paper.pdf) and [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Mehlführer_poster.pdf)

*Advised by {{% mention "christian-huemer" %}}*