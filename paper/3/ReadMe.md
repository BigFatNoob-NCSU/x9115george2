# Summary 
## (i) Reference : Jian Hu, Gang Wang, Fred Lochovsky, Jian-tao Sun and Zheng Chen @ www 2009. Understanding user's query intent with wikipedia. [Paper](https://http://dl.acm.org/citation.cfm?id=1526773)

## (ii) Keywords

  * (ii1)**Pattern Recognition** : Pattern recognition is a branch of machine learning that focuses on the recognition of patterns and regularities in data, although it is in some cases considered to be nearly synonymous with machine learning.(wiki)
  * (ii2)**Information Search** : Information search refers to retrieving relevant information using various sources. Its a part of consumer decision process where a consumer looks for internal or external information(wiki).
  * (ii3)**Wikipedia** : Wikipedia is a multilingual, web-based, free content encyclopedia written collaboratively by more than 75,000 regular editing contributors. Its articles can be edited by anyone with access to its website.
  * (ii4)**Query Classification**  : A Web query topic classification/categorization is a problem in information science. The task is to assign a Web search query to one or more predefined categories, based on its topics. The importance of query classification is underscored by many services provided by Web search. (wiki)

## (iii) Artifacts
  * (iii1) **Motivation** : Current approaches to predict the user's intent mainly utilize machine learning techniques. But, it is difficult and often requires a lot of human effort to meet all the challenges posed by statistical machine learning methods. Currently(2008), a user has to identify his intent in advance and decide which vertical search engine to choose to satisfy his intention. It would be convenient if a query intent identifier could be provided in a general search engine that could accurately predict whether a query should trigger a vertical search in a certain domain. Two primary challenges that query intent analysis possess are 
   * **_Domain Coverage Challenge_** : . If the input samples only cover a subset of concepts in an intent domain, the learned classifier cannot make good predictions for those queries that are not covered by the training samples.
   * **_Semantic Interpretation Challenge_** : This defines how to correctly understand the semantic meaning of the input query. Previous works attempted to solve this problem through augmenting the query with more features using external knowledge, such as search engine results.
  * (iii2) **Hypotheses** : With very little human effort, the proposed method can discover large quantities of intent concepts by leveraging Wikipedia, one of the best human knowledge base. The Wikipedia concepts are used as the intent representation space, thus, each intent domain is represented as a set of Wikipedia articles and categories. Compared with previous approaches, the proposed method can achieve much better coverage to classify queries in an intent domain even through the number of seed intent examples is very small. Moreover, the method is very general and can be easily applied to various intent domains.
  * (iii3) **Checklist** : 
   * Wikipedia concepts as the intent representation, and each intent domain is represented as a set of Wikipedia articles and categories. Initial seed examples are identified using minimal human effort.
   * Wikipedia includes nearly every aspect of human knowledge and is organized hierarchically as an ontology. Markov random walk algorithm is used iteratively to propagate the intent from the seed examples into the Wikipedia ontology and assign an intent score to each Wikipedia concept. Hence an intent probability for each concept in Wikipedia, which clearly identifies the semantic boundary of the intent domain
   * Each query is mapped into a Wikipedia representation. If the input query can be exactly mapped to a Wikipedia concept, it can easily predict the query's intent based on its associated intent probability. Otherwise, the query is mapped to the most related Wikipedia concepts using explicit semantic analysis (ESA), and the judgment is based on the intent probabilities of mapped Wikipedia concepts, which overcomes the semantic disambiguation issue.
  * (iii4) **Patterns and Anti Patterns** :
   * **_Patterns_** : 
    * In predicting future unseen data, two conditions should be satisfied: discriminative feature representation and sufficient training samples.  
    * For query intents not covered by wikipedia, explicit semantic analysis (ESA) is used, which utilizes Wikipedia for feature generation for the task of computing semantic relatedness. Empirical evaluation indicates that using ESA leads to substantial improvements in computing relatedness between words and text, and the correlation of computed relatedness of ESA with human judgments is much better than previous states of the art.
    * TFIDF is used to quantify relation between words and concepts. An inverted index is constructed, to speed up the semantic interpreter which maps each word into a list of Wikipedia concepts in which it appears.
   * **_Anti Patterns_** :
    * If the training data is too sparse, for query intent classification, discriminative feature representation and sufficient training samples are hardly met together.
    * If the input samples only cover a subset of concepts in an intent domain, the learned classifier cannot make good predictions for those queries that are not covered by the training samples.
    * If a user’s input query is ambiguous according to the Wikipedia disambiguation pages, the method will not make any intent prediction for this query.
  * (iii5) **Related Work** :
   * **_Enriching queries using web search engines_**: D. Shen, J. Sun, Q. Yang, and Z. Chen. Building bridges for web query classification. In Proc. of the 29th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR-06), 2006
   * **_Search result snippets as query features_** : A. Broder, M. Fontoura, E. Gabrilovich, A. Joshi, V. Josifovski, and T. Zhang. Robust classification of rare queries using web knowledge. In Proc. of the 30th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR-07), July 2007
   * **_Binary classifier to detect query's online commercial intent_** :  Honghua (Kathy) Dai, Lingzhi Zhao, Zaiqing Nie, Ji-Rong Wen,Lee Wang, Ying Li: Detecting online commercial intention(OCI). In Proc. of the 15th World Wide Web Conference (WWW-06), 2006.
   * **_Augmenting unlabeled data with semi supervised training_** : S. Beitzel, E. Jensen, O. Frieder, D. Lewis, A. Chowdhury, and A. Kolcz. Improving automatic query classification via semisupervised learning. In Proc. of the 5th IEEE International Conference on Data Mining(ICDM-05), 2005

## (iv) Improvisations:
  * (iv1) They say that the graph processing takes linear time to obtain query results, but they do not mention that based on their methods, it would take polynomial time to construct the graph and also iteratively keep updating it.
  * (iv2) They do not explain why they use ngrams of size 1 and 2. Probably, magic parameters but they should then have tried for different values or given appropriate justification
