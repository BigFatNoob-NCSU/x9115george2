# Summary 
## (i) Reference : Marek Gibiec, DePaul University and Jane Cleland-Huang ASE-2010. Towards Mining Replacement Queries for Hard-to-Retrieve Traces. [Paper](http://dl.acm.org/citation.cfm?id=1859046)

## (ii) Keywords

  * (ii1)**Requirements** : In a software system requirement is a functional need that a particular design, product or process must be able to perform.
  * (ii2)**Information Search** : Information search refers to retrieving relevant information using various sources. Its a part of consumer decision process where a consumer looks for internal or external information(wiki).
  * (ii3)**Requirements Tracability** : It defines the ability to track down the life of a requirement back to its source documents. The source documents can range from databases, spreadsheets, flat files etc.
  * (ii4)**Text Mining**  : Text mining is the process of retrieving relavant information from chunks of textual information. Feature weighting techniques like TF-IDF can be used to identify significant words. POSTaggers and stemmers can be used to remove insignificant words

## (iii) Artifacts
  * (iii1) **Motivation** : Automated Trace retrieval methods significantly reduce cost and effort involved in requirement traces. But many a times, it  is not possible to find relevant links for a query. In such cases a human needs to intervene to manually search for relavant links by modifying the query and/or rejecting links that are not helpful. In many non-trivial projects the number of search links are very large(in order of thousands). In such cases, it is hard to manually select or reject links. Techniques like Latent Semantic Indexing, Vector space models and probabilistic approaches show that although the traceablity effort in projects are reduced, the traces generated are not very precise and additionally required an analyst to evaluated the resuts to obtain the right set of links.
  * (iii2) **Hypotheses** : Based on the initial motivation and relavant work, the authors observed that low precision was caused due to a few stubborn results which reduced the overall quality of the generated results. Based on the paper, stubborn traces occur when language in the document neither matches the language of the source document nor matches the project level synonyms defined in a thesaurus. The paper addresses automating the web mining process using various search engines and implementing and validating a technique for identifying appropriate sections of text from retrieved documents.
  * (iii3) **Related Work** :
   * Traces using Vector Space Model : Hayes, J. H., Dekhtyar, A., and Sundaram, S., (2006), "Advancing Candidate Link Generation for Requirements Tracing: The Study of Methods", IEEE Transactions on Software Engineering, vol. 32, no. 1, January, pp. 4-19.
   * Traces using probabilistic approaces : Cleland-Huang, J., Settimi, R., Duan, C., and Zou, X., (2005b), "Utilizing Supporting Evidence to Improve Dynamic Requirements Traceability", IEEE International Conference on Requirements Engineering (RE), pp. 135-144.
   * Traces using LSI : Maletic, J. I. and Marcus, A., "Using Latent Semantic Analysis to Identify Similarities in Source Code to Support Program Understanding", in Proceedings of 12th IEEE Int‟l Conf. on Tools with Artificial Intelligence, Vancouver, British Columbia, 2000, Nov 13-15, pp. 46-53.
   * Comparing machine learning techniques on trace results : Cleland-Huang, J., Czauderna, A., Gibiec, M., Emenecker, J., “A Machine Learning Approach for Tracing Regulatory Codes to Product Specific Requirements”, International Conf on Software Eng., Cape Town, South Africa, May, 2010.
   * Using Wikipedia to augent web based search queries : Hu, J., Wang, G., Lochovsky, F., Sun, J. and Chen, Z. Understanding user's query intent with wikipedia. 18th International Conference on World Wide Web, Madrid, Spain, April 20-24, 2009 (WWW'09). 471-480.
  * (iii4) **New Results** :
   * A combination of Bing, Google and Yahoo yielded the best results.
   * Retrieving large number of documents did not yield improved results. Rather the top results obtained using the right query yielded better precision
   * Smaller chunks yielded better precision(6/10) compared to larger chunks.
   * Concept Generality ranged from 0.02-0.6, Domain Specificity Ranged from 10-140 and Term Frequency ranged from 0.1-0.9.
   * The approach does not uniformly improve every trace query. THe augmented query returned only perfect scores for 7 of the 11 queries exibiting perfect result with the basic method.

## (iv) Improvizations:
  * (iv1) Search engines does not significantly change the precision. So they could have compared results against other methods.
  * (iv2) Figures depicting new results vs base results would give a better insight would be better.
  * (iv3) Along with precision and recall, measures of false alarm rate and g score would have given a better insight on the results

