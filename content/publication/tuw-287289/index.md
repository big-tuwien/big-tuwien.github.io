---
abstract: Modern tools for developing software have added a plethora of capabilities
  to support software engineers in their daily work. These tools do not only provide
  simple features based on the words in a file, but parse and understand the code,
  and extract the underlying structure. Especially operations for refactoring have
  become more and more sophisticated. It is possible with a couple of clicks to change
  the signature of methods, move classes, extract variables, and structurally search
  and replace code snippets. These advances in writing new code and adapting existing
  code have been a major advantage for developers. While integrated development environments
  and editors like IntelliJ IDEA can perform more and more operations based on the
  structure of the source code, tools for reviewing code are still stuck with the
  textual representation of the code. The difference between two versions of the source
  code is calculated line by line, word by word, character by character without any
  regard for the semantic meaning and tree-like structure of source code. Diff algorithms
  which work on the abstract syntax trees can, for example, mark changes in the code
  which have no effect on the runtime behavior of the program. If, for example, a
  programmer changes the formatting of the code, this will result in many detected
  changes when using classic text-based algorithms. Semantic diff algorithms could
  hide these changes so that a reviewer can focus on semantically relevant changes.
  The goal of this thesis is to take existing algorithms for calculating the difference
  between two versions of source code in a tree structure and extend them to work
  with multiple programming languages. Current Version Control Systems are tracking
  the changes only on actions of software engineers to track change between certain
  points in the history. This results in a loss of information between these points
  in time. To remedy that, the semantic diff algorithms are combined with approaches
  to continuously track changes of source code without relying on the developer to
  record fixed points in time with explicit commits. A qualitative user study tests
  the usefulness of the resulting prototype, where developers try to answer questions
  about source code in four different scenarios. The usability of the tool is judged
  by the participants of the user study based on the System Usability Scale and reached
  an overall value of 73,75.
authors:
- Matthias Sperl
date: '2019-01-01'
featured: false
publication_types:
- '7'
publishDate: '2019-01-01'
title: A Method for Semantic Patches of Multiple Programming Languages Based on Continuously
  Captured Changes
url_pdf: ''
---