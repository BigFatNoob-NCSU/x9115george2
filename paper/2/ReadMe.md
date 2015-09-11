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
  * (iii5) **New Results** :

## (iv) Improvisations:
  * (iv1) 
  * (iv2) 
  * (iv3) 
