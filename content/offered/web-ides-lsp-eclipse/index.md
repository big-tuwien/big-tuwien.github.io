---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Web IDEs & Language Server Protocol (LSP) – in collaboration with EclipseSource"
subtitle: ""
summary: ""
authors: []
tags: []
categories: []
date: 2020-04-25T20:45:21+02:00
lastmod: 2020-04-25T20:45:21+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

There is currently a large hype surrounding Web IDEs and the language server protocol (LSP). LSP provides a very flexible and well-proven architecture for implementing textual editors. It allows to reuse editor implementations for different languages by decoupling editor implementations from language implementations in so-called language servers. Through this decoupling, also Web-based IDEs become easily implementable.

Wouldn’t it be cool to use a similar protocol and architecture for graphical modeling languages, too? Following in the footsteps of LSP, this would make it possible to implement a “generic diagram editor” that talks to a graphical language server, retrieving information on the modeling language such as how nodes are rendered, how they can be connected, or which elements can be created from a palette.

A protocol-based implementation for graphical editors in the web sounds like an obvious follow-up of LSP. However, diagrams are not the same as source code, they have fundamentally different editing features, such as complex combinations of shapes that can be connected, resized, or nested with drag and drop. To find out what’s possible and what makes sense, we have started the implementation of a proof of concept for such a Graphical Language Server Protocol (GLSP) along with demonstrators for language servers and generic diagram editors.
The obvious starting point for this was the open source framework Sprotty, a new graphical framework in the Eclipse ecosystem. It already contains a protocol (an extension to LSP) to synchronize graphs from a server to the client. Therefore, we started to extend Sprotty by new protocol parts, such as editing, a palette concept, and possible node references.

We are offering Bachelor’s theses, Master’s theses, as well as internships around this topic. The focus of your work can be chosen individually. Possible topics are for example the following:
* The extension and evaluation of the GLSP protocol
* The implementation and evaluation of a particular language server (e.g., for UML)
* The development of novel interaction features of Web-based diagram editors
* The improvement of the user experience (UX) of Web-based diagram editors

If you are interested in this topic, contact Dr. Philip Langer from the company EclipseSource <planger@eclipsesource.com>, who will supervise your work on this topic.
