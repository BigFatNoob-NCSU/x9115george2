# Summary
## (i) Reference :Nan Niu and Anas Mahmoud @International Requirements Engineering Conference 2012. Enhancing Candidate Link Generation for Requirements Tracing: The Cluster Hypothesis Revisited. [Paper](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=6345842)

## (ii) Keywords

  * (ii1)**Requirements** : A requirement in product development and process optimization is a singular documented physical and functional need that a particular design, product or process must be able to perform.
  * (ii2)**Information Search** : Information search refers to retrieving relevant information using various sources. Its a part of consumer decision process where a consumer looks for internal or external information(wiki).
  * (ii3)**Clustering** : Clustering is an unsupervised learning method which automatically divides data into natural groups based on similarity.
  * (ii4)**Traceability** : Traceability is the ability to verify the history, location, or application of an item by means of documented recorded identification(wiki).  

## (iii) Artifacts
  * (iii1) **Motivation** :
    * Due to the inherent trade-off between recall and pre- cision, information retrieval methods cannot achieve a high coverage without also retrieving a great number of false positives, causing a significant drop in result accuracy.
    * Traceability has since been shown to be critical for a wide variety of software engineering activities, including verification and validation (V&V), risk assessment, and change impact analysis. However, practitioners often fail to implement consistent and effective traceability processes if the traces are maintained manually.
    * Currently, IR-based tracing tools favor recall over pre- cision. This is mainly because commission errors (false positives) are easier to deal with than omission errors (false negatives). However, retrieving an excessive number of links can seriously affect the practicality of such tools.
    * The overarching goal of the proposed method is to capture all potential correct traceability links and incorrect ones.
  * (iii2) **Hypotheses** : 
    * Clustering will be able to group correct and incorrect links can be grouped in high-quality and low-quality links respectively. Thus, the performance of IR-based tracing can be enhanced by selecting candidate links from high-quality clusters.
    * The problem of consistency and effectiveness can be overcome by automatic generation of traceability links by exploiting Information Retrieval methods like Vector Space Model, Probablistic Network Model adn Latent Semantic Indexing.
    * The proposed method advances the fundamental understanding about the role clustering plays in traceability, but also enables principled ways to increase the practicality of automated tracing tools.
  * (iii3) **Patterns / Anti-Patterns** :
    * **_Patterns_** :
      * To improve system performance clustering is first performed and aand then the query is matched to the cluster centroids.
      * Organizing and displaying the retrieved artifacts in topic-coherent clusters can facilitate the comprehension and evaluation of the search results.
      * Pruning false positives to filter the result list can present the human analyst only a subset of retrieved links.
      * Clustering is performed only after initial search. This makes clustering dynamic rather than static.
      * Heurestics can be used automatically differentiate between high quality and low quality clusters.
      * Filtering a link considers the similarity to the query as well as the cluster the link belongs to.
    * **_Anti Patterns_** :
      * As the number of documents increases, matching the query to all documents can degrade the system performance.
      * The searchable artifacts in tracing consist of individual requirements, classes and test cases. Such a collection tends to be significantly smaller than the document collection targeted in a typical Web search or online library search. Therefore, the need of reducing the search space via document clustering is less pressing in requirements tracing.
      * Ideally every requirement is concise, primitive, and unambiguous, the reality is that requirements can often be relatively long and may also contain superfluous information.
  * (iii4) **Related Work** :
    * **_Identifying candidate links using Vector Space Modeling_** : J. H. Hayes, A. Dekhtyar, and S. K. Sundaram, “Advancing candidate link generation for requirements tracing: the study of methods,” IEEE TSE, vol. 32(1), pp. 4–19, 2006.
    * **_Applying Probabilistic Network Models for Traceability_** : J. Cleland-Huang, R. Settimi, C. Duan, and X. Zou, “Utilizing supporting evidence to improve dynamic requirements traceability,” in RE, 2005, pp. 135–144.
    * **_Latent Semantic Indexing for candidate link generation_** : A. Marcus and J. I. Maletic, “Recovering documentation-to-source- code traceability links using latent semantic indexing,” in ICSE, 2003, pp. 125–137.
    * **_Comparitive Study on all the state of the art methods_** : R. Oliveto, M. Gethers, D. Poshyvanyk, and A. De Lucia, “On the equivalence of information retrieval methods for automated traceabil- ity link recovery,” in ICPC, 2010, pp. 68–71.

## (iv) Improvisations:
  * (iv1) The research questions could be addressed explicitly. It was hard to identify the solutions of the reseach questions within the paper.
  * (iv2) Density Based Clustering methods can be used to identify the clusters. It could be used to identify frequent clusters.
