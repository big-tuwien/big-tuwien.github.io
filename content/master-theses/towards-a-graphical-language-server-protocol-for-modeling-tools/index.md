---
authors:
- Tobias Ortmayr
categories: []
date: '2020-05-08 15:44:44+00:00'
external_link: ''
image:
  caption: ''
  focal_point: ''
  preview_only: false
slides: ''
summary: ''
tags:
- Ongoing
title: Towards a Graphical Language Server Protocol for Modeling Tools
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

The use of graphical concrete syntax is one of the most common approaches to&nbsp;express and visualize the concepts of a modeling language. With the help of specialized modeling tools developers are able to create and edit models based on&nbsp;their graphical representation. Traditional graphical modeling editors are&nbsp;powerful, heavy weight desktop applications that are strongly tailored towards&nbsp;a particular language and built on top of existing modeling frameworks like the&nbsp;Eclipse Modeling Framework (EMF). This causes major limitations in terms&nbsp;of re-usability and extensibility. It’s often not possible to develop a graphical&nbsp;language that is supported by multiple modeling tools without major modications and the anguage has to be integrated into each platform/tool separately.&nbsp;Another aspect that has to be considered is the rise of web technologies, and&nbsp;in particular cloud based concepts, that can be observed over the last couple&nbsp;of years. This trend causes a shift in Model-Driven Engineering resulting in an&nbsp;increased interest to migrate existing model editing tools to the web. The motivations driving this shift are twofold: increased usability through the usage of&nbsp;modern UI technology, such as TML5 and CSS, and simplied deploy ability&nbsp;via a browser. In addition, this enables new opportunities like cloud-based collaborative modeling tools but at the same time opens new challenges and potential&nbsp;problems. Web-based solutions require a decoupled architecture composed of&nbsp;dedicated client and server artifacts. However due to their monolithic nature&nbsp;current state of the art modeling tools are not suitable for distributed deployment. The development of full- edged graphical modeling tools is a challenging&nbsp;and complex task \[15\] so re-implementing them on a web-based technology stack&nbsp;is often not feasible. Instead a proper approach to develop and maintain modern&nbsp;web modeling tools whilst reusing well established modeling platforms has to be&nbsp;found.  
 These problems are not only limited to the context of graphical languages but&nbsp;are also applicable to other language development areas. Looking at textual programming languages similar issues have been concluded and led to the creation of  
 the Language Server Protocol (LSP). This eort eectively decouples textual&nbsp;language IDE development into a client-server architecture. The client is generic&nbsp;and language-agnostic which means an LSP client can (potentially) connect to  
 any number of language-specic servers via standardized protocol.&nbsp;Following a similar path for graphical languages seems logical but it’s currently&nbsp;not clear how to properly achieve this. Technically LSP provides a powerful&nbsp;extension mechanism which would allow the implementation of a graphical language server protocol on top of LSP. In practice this approach has some major&nbsp;downsides and might even be insucient to cover all common use cases. In order  
 to use LSP each graphical language would have to conform to a textual language. Since not all potential graphical languages are or even can be derived&nbsp;from textual artifacts another solution might be preferable.  
 It also has to be considered that the concept of completely language-agnostic&nbsp;clients might not be applicable in this context. Graphical language clients need&nbsp;a lot additional information to properly identify model elements, render their  
 graphical representation and to be able to trigger model modications.

*Advised by {{% mention "gertrude-kappel" %}}*