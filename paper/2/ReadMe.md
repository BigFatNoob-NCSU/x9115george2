# Summary 
## (i) Reference : Jane Cleland-Huang, Adam Czauderna, Marek Gibiec and John Emenecker ICSE-2010. A machine learning approach for tracing regulatory codes to product specific requirements. [Paper](https://github.com/BigFatNoob-NCSU/x9115george2/blob/master/paper/2/A%20machine%20learning%20approach%20for%20tracing%20regulatory%20codes%20to%20product%20specific%20requirements.pdf)

## (ii) Keywords

  * (ii1)**Requirements Tracability** : It defines the ability to track down the life of a requirement back to its source documents. 
  The source documents can range from databases, spreadsheets, flat files etc.
  * (ii2)**Information Search** : Information search refers to retrieving relevant information using various sources. Its a part of
  consumer decision process where a consumer looks for internal or external information(wiki).
  * (ii3)**Machine Learning** : Machine learning explores the study and construction of algorithms that can learn from and make 
  predictions on data. Such algorithms operate by building a model from example inputs in order to make data-driven predictions or 
  decisions, rather than following strictly static program instructions(wiki).
  * (ii4)**Web Mining**  : Web mining is the use of data mining techniques to automatically discover and extract information from 
  Web documents and services(wiki).

## (iii) Artifacts
  * (iii1) **Motivation** : Current methods for checking requirements compliance rely on standard software engineering practices of requirements traceablity which is the ability to track a requirement from its origins back to its rationale and downstream to various work products that implement that requirement in software. Manual tracing can be prohibitively time-consuming; however automated trace retrieval methods are not very effective due to the vocabulary mismatches that often occur between regulatory codes and product level requirements. Current(upto 2010) studies show that organizations struggle to implement successful and cost-effective traceability, primarily because creating, maintaining, and using traces is a time-consuming, costly, arduous, and error prone activity. Moreover efficient information retrieval and data mining techniques have not been explored based on the literature which leaves an avenue open.
  * (iii2) **Hypotheses** : Two methods were proposed in the paper. The first approach uses manually created traceability matrices to train a trace classifier, while the second approach uses web-mining techniques to reconstruct the original trace query. Machine learning methods are appealing for tracing regulatory codes, because the upfront effort of training a classifier can be potentially recouped when same codes are applied across future projects. The hypothesis behind the web mining approach is that a relevant set of indicator terms can be learned from domain specific documents mined from the Internet
  * (iii3) **Patterns and Anti Patterns** :
   * **_Patterns_** : 
     * Automated methods have generally been quite effective, returning a candidate set of traces that contain 85- 90% of the targeted links at precision rates of 10-50%.
     * Although precision was low, basic automated methods excluded a large number of unlikely links.
     * For the machine learning approach, from a series of initial experiments selecting the top 10 terms for each of the requirement types returned optimal classification results in comparison to other selection methods.
     * _Concept Generality_ threshold for a term is optimal at 0.3 and the maximum _Domain Specificity_ for a term is set to 5.
   * **_Anti Patterns_** :
     * Automated methods have limited success for tracing regulatory codes[4] due to the significant disparity in terminology that can exist between the codes and product level requirements.
     * Basic Automated methods yielded low precision values(Range of 0.02)
     * Additional error is introduced when human analysts are asked to evaluate a long list of candidate links genereated by the automated methods.
  * (iii4) **Related Work** :
   * **_Traces using Vector Space Model_** : Hayes, J. H., Dekhtyar, A., and Sundaram, S., (2006), "Advancing Candidate Link Generation for Requirements Tracing: The Study of Methods", IEEE Transactions on Software Engineering, vol. 32, no. 1, January, pp. 4-19.
   * **_Traces using probabilistic approaces_** : Cleland-Huang, J., Settimi, R., Duan, C., and Zou, X., (2005b), "Utilizing Supporting Evidence to Improve Dynamic Requirements Traceability", IEEE International Conference on Requirements Engineering (RE), pp. 135-144.
   * **_Traces using Latent Semantic Indexing_** : Maletic, J. I. and Marcus, A., "Using Latent Semantic Analysis to Identify Similarities in Source Code to Support Program Understanding", in Proceedings of 12th IEEE Int‟l Conf. on Tools with Artificial Intelligence, Vancouver, British Columbia, 2000, Nov 13-15, pp. 46-53.
   * **_Using Wikipedia to augent web based search queries_** : Hu, J., Wang, G., Lochovsky, F., Sun, J. and Chen, Z. Understanding user's query intent with wikipedia. 18th International Conference on World Wide Web, Madrid, Spain, April 20-24, 2009 (WWW'09). 471-480.
   * **_General web knowledge to augment queries_** : Breaux, T.D. and Anton, A.I. Analyzing Regulatory Rules for Privacy and Security Requirements IEEE Transactions on Software Engineering, 2008, 5-20.
  * (iii5) **New Results** :
   * The machine learning approach did not improve traceability for the five HIPAA goals that performed best under the basic traceability approach; however it did significantly improve results for four of the five HIPAA goals that had not previously performed well.
   * The web mining approach outperformed the basic approach for three of the same HIPAA regulations that were improved by the machine learning method; these were access control, audit control and personal authentication. Although improvements in average precision were less than those achieved by the machine learning method, the human effort was also significantly less. The web mining approach also improved results for integrity which the machine learning approach had been unable to do. However the web-mining approach performed worse on four of the HIPAA regulations than either of the other methods.

## (iv) Improvisations:
  * (iv1) Sources for tInformation retrieval and preprocessing techniques like stop word removal could have been provided.
  * (iv2) Source code repository for implementation could have been given for future experiments.
  * (iv3) Pearson's correlation technique was used for comparing the techniques. Rather, the authors could have used statistical ranking techniques like scott-knott to check if the techniques are statistically different from each other.
