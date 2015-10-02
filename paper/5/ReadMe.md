# Summary
## (i) Reference : Giuliano Antoniol, Gerardo Canfora, Gerardo Casazza, Andrea De Lucia and Ettore Merlo @TSE 2002. Recovering Traceability Links between Code and Documentation. [Paper](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=1041053)

## (ii) Keywords

  * (ii1)**Requirements Tracability** : It defines the ability to track down the life of a requirement back to its source documents. The source documents can range from databases, spreadsheets, flat files etc.
  * (ii2)**Information Search** : Information search refers to retrieving relevant information using various sources. Its a part of consumer decision process where a consumer looks for internal or external information(wiki).
  * (ii3)**Object Orientation** : Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which are data structures that contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods(wiki).
  * (ii4)**Program Comprehension**  :  Program comprehension is a vital software engineering and maintenance activity. It is necessary to facilitate reuse, inspection, maintenance, reverse engineering, reengineering, migration, and extension of existing software systems

## (iii) Artifacts
  * (iii1) **Motivation** :
    * Traceability links between areas of code and related sections of free text documents, such as an application domain handbook, a specification document, a set of design documents, or manual pages, aid both top-down and bottom-up comprehension.
    * Traceability links between code and other sources of information are a sensible help to perform the combined analysis of heterogeneous information and, ultimately, to associate domain concepts with code fragments.
    * Traceability links between the requirement specification document and the code are a key to locate the areas of code that contribute to implement specific user functionality. This helps assess the completeness of an implementation with respect to stated requirements, to devise complete and comprehensive test cases, and to infer requirement coverage from structure
coverage during testing. Traceability links between requirements and code can also help to identify the code areas directly affected by a maintenance request as stated by an end user
    * A major goal of impact analysis is the identification of the work products affected by a proposed change.
    * Means to trace code to free text documents are a sensible help to locate reuse-candidate components.
  * (iii2) **Hypotheses** : 
    * Recovering traceability links between free text documentation and source-code components cannot be simply based on compiler techniques because of the difficulty of applying syntactic analysis to natural language sentences.
    * The premise of the work is that programmers use meaningful names for program items, such as functions, variables, types, classes, and methods. The analysis of mnemonics can help to associate high-level concepts with program concepts, and vice-versa. The names of program items are used as a clue to suggest concepts implemented in the code.
    * An assumption that programmers use meaningful names for their identifiers and/or that indetifiers are preprocessed to extract names that share the semantics of the requirements.
  * (iii3) **Commentary** :
    * Probabilistic Model: Free-text documents are ranked according to the probability of being relevant to a query computed on a statistical basis. To compute this ranking, the idea of a language model is exploited, i.e., a stochastic model that assigns a probability to every string of words taken from a prescribed vocabulary. A language model is estimated for each document, or identifiable section, and use a Bayesian classifier to score the sequences of mnemonics extracted from each source code component against the models. A high score indicates a high probability that a particular sequence of mnemonics be relevant to the document; therefore, it is intepreted as an indication of the existence of a semantic link between the component from which the sequence had been extracted and the document. 
    * Vector Space Model: Vector space model treats documents and queries as vectors in an n-dimensional space, where n is the number of indexing features. Documents are ranked against queries by computing a distance function between the corresponding vectors. In this paper, the documents are ranked according to a widely used distance function, i.e., the cosine of the angle between the vectors.
  * (iii4) **New Results** :
    * The probabilistic model achieves higher values of recall with smaller cut values and makes little progress towards 100 percent of recall. On the other hand, the vector space model starts with lower recall values and makes regular progress with higher cut values towards 100 percent of recall.
    * The probabilistic model is more suitable for cases where the presence of code component identifiers that do not belong to the software document is low.
    * The vector space model does not aim for the best match, but rather to regularly achieve the maximum recall with a moderate number of retained documents.
    * Unlike the probabilistic model, the vector space model is able to achieve higher recall values based on a smaller number of relevant words in a source code component.
## (iv) Improvisations:
  * (iv1)
  * (iv2)
