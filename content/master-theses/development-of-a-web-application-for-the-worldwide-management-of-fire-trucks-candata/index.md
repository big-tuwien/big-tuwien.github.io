---
authors:
- Thomas Bruckmayer
categories: []
date: '2020-05-08 14:38:41+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: Development of a Web Application for the Worldwide Management of Fire Trucks
  CAN-Data
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in October 2009.

In a technologically improving world the effective execution of business processes and workflows requires a lot of knowledge and information. As a consequence a sustainable knowledge management and sophisticated tool support are extremely important for every successfully operating company. Within an extremely wide range of tools, Web applications gain more and more importance to meet the constantly increasing requirements. Outstanding benefits are worldwide accessibility and interoperability on a very large scale. Moreover, in many cases no installation on single clients is needed, updates can be provided easily, and centralized data management on the server-side avoids costly synchronizations. These factors lead to reduced costs for the information infrastructure and support the employees to do their work. For example, a constructor of firefighting cars can query the headquarters database on the other side of the world to find out which CAN data (Controller–area network) is needed to configure a specific vehicle.

Building such solutions is not a trivial task and therefore disciplines like Web Engineering and Internet Computing emerged. Furthermore, developers can choose from a wide range of technologies to realize their solutions. Handling these technologies leads to successful development of Web Applications.

This master’s thesis describes in detail the solution for a specific problem in the industry, namely a Web application called CORA to manage the CAN-Data for Rosenbauer International AG. According to the company’s it-infrastructure MSSQL Server, IIS, and ASP.NET had been chosen as core technologies. On one hand the .NET framework provides the possibility to develop applications in a rather short time, also known as Rapid Application Development (RAD). On the other hand many RAD-techniques are not applicable on large enterprise solutions where the complexity has to be broken down to several layers. This work presents approaches, patterns and techniques for each layer.

The Data Access Layer is responsible for retrieving data and uses Linq to SQL as object relational mapper. In addition the possibilities of model driven development to create the fundamental data manipulation objects will be evaluated. The Business Layer handles the communication between the Data Access Layer and the Presentation Layer and adds business functionality. Finally, the Presentation Layer presents the data in an appropriate format and handles the user interaction.

Furthermore, the database schema of the sample application has been constantly renewed and improved to cover additional requirements like multiple CAN bus systems, multilingualism, user administration, and a history of important entities. Therefore, schema evolution and data migration has played an additional important role in this thesis.

All these aspects have been elaborated theoretically and explained practically with the help of CORA. Consequently, this thesis provides a method in state of the art web application development for small business projects.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Bruckmayer_papers.pdf) and [poster](https://www.big.tuwien.ac.at/app/uploads/2016/10/Bruckmayer_poster.pdf)

*Advised by {{% mention "petra-kaufmann" %}}, {{% mention "gertrude-kappel" %}}*