---
advisors:
- gertrude-kappel
authors:
- Hans Moritsch
categories: []
date: '2020-05-19 12:38:21+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Finished
title: High Performance Computing in Finance - On the Parallel Implementation of Pricing
  and Optimization Models
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

This work has been finished in May 2006.

High Performance Computing is useful in the field of finance for solving problems which are defined on models of financial variables in the form of sequences of scenarios along with their realization probabilities. Both the evolution of stock prices and interest rates is frequently described in this manner. Starting from a known state, and covering a future time horizon of multiple periods, these models take the form of scenario trees. As a special case, the structure collapses into a lattice, if the tree is “recombining”. This work deals with the two problem classes of determining prices of financial instruments, and of determining optimal portfolios of assets, with respect to some objective function and constraints. Dynamic optimization techniques allow for multiple planning periods, whereas stochastic dynamic optimization problems take into account also probabilities and exhibit (exponentially growing) tree structures, which can become very large. As an example, a model of ten years of three assets, each of which is described by the extents and probabilities of rising or falling of their respective prices within a year, results in a scenario tree with more than one billion (23 )10 = 1 073 741 824 terminal nodes. Computation times for solving these problems can extend to hours and days, hence high performance computing techniques of achieving speed up are desirable.

The major approach for performance improvement in this work is parallel computing. It includes the parallel implementation of Monte Carlo simulation techniques as well as of backward induction methods for pricing path dependent interest rate derivatives, in particular constant maturity floaters with embedded options. In the optimization part, the nested Benders decomposition method of multistage stochastic optimization has been parallelized in a synchronous as well as in an asynchronous version. The parallel implementations obtain speedups ranging from reasonable to excellent and demonstrate the potential of high performance computing for financial applications. In addition, they served as case studies in the development of software tools for high performance computing within the framework of the Special Research Program No. F011 Aurora “Advanced Models, Applications and Software Systems for High Performance Computing” of the Austrian Science Fund (FWF).

The data parallel programming language HPF+, with extensions for clusters of SMPs, has been successfully employed in the implementation of pricing algorithms. A path notation has been specified as an extension to Fortran 95, allowing for the high level formulation of parallel algorithms operating on lattice structures. The parallel programming model of a distributed active tree has been designed and implemented on top of Java’s threads and RMI. Parallel implementations of the nested Benders decomposition algorithm in Java demonstrate that this is a suitable language for high performance computing. The OpusJava component framework, as well as the JavaSymphony class library, and the distributed active tree model proved their usefulness as programming support environments in the implementation of parallel tree structured algorithms.

In addition to the parallelization of sequential existing algorithms, the improvement of known parallelization approaches, and the use of specialized parallel programming languages and programming models, an increase in performance has been achieved by algorithmic developments. The generalization of the classical backward induction method allows for the faster calculation, i.e., in linear instead of exponential time, of prices of a class of instruments exhibiting “limited” path dependence, demonstrating that highly effective approaches of performance improvement combine the levels of algorithms and parallel implementation.

&nbsp;

 Download the [paper](https://www.big.tuwien.ac.at/app/uploads/2016/10/Moritsch_H.pdf)