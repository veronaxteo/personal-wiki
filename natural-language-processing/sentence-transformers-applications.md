# applications of sentence transformers

## notes based off of SBERT

### semantic textual similarity
- after computing sentence embeddings of corpus, we can compare them to each other using cosine similarity between embeddings to measure the semantic similarity of texts
- can also find out the pairs with the highest cosine similarity scores
- these use a brute-force approach to find the highest scoring pairs, so it has a quadratic complexity
	- thus, might not be feasible for long lists of sentences
	- might be better to do *paraphrase mining* instead


### retrive & re-rank
- for complex search tasks, e.g. Q&A retrieval, semantic search can be significantly improved by using retrieve & re-rank

#### pipeline
- given search query, first use a *retrieval system* that retrieves large list of possible hits which are potentially relevant for query
	- can either lexical search or use dense retrieval with bi-encoder
- but retrieval system might retrieve documents that are not very relevant, so have second stage that uses a *re-ranker* based on a cross-encoder that scores relevancy of all candidates for given search query
- output is ranked list of hits presented to user

![[retrieve-rerank-pipeline.png]]


### semantic search
- improve search accuracy by understanding content of search query
	- unlike traditional search engines which only find documents based on lexical matches, semantic search can also find synonyms

- idea: embed all entries in your corpus into a vector space
	- at search time, query is embedded into same vector space and the closest embeddings from the corpus are found
		- these entries should have high semantic overlap with the query

#### symmetric vs asymmetric semantic search
- **symmetric semantic search** - query and entries of corpus are of *about the same length and have the same amount of content*
	- ex: query = "how to learn python online?", entry = "how to learn python on the web?"

- **asymmetric semantic search** - usually have a *short query* and you want to find a longer paragraph answering the query
	- ex: query = "what is python", find paragraph "python is an interpreted, high-level and general-purpose programming language. python's design ... "

- important to choose right model for type of task


### clustering
#### k-means
- k-means requires that number of clusters is specified beforehand
- sentences are clustered in groups of about equal size

#### agglomerative clustering
- **hierarchical clustering** using **agglomerative clustering algorithm**
- unliked k-means, can specify a *threshold* for clustering
	- clusters below threshold are merged
- this algorithm can be useful if number of clusters is unknown
- can be slow for larger datasets; applicable for ~a few thousand sentences

#### fast clustering
- clustering algorithm that is tuned for large datasets (50k sentences in less than 5 secs)
- in large list of sentences, it searches for *local communities*, a set of highly similar sentences

#### topic modeling
- process of *discovering topics in a collection of documents*
- tutorial: [Topic Modeling with BERT](https://towardsdatascience.com/topic-modeling-with-bert-779f7db187e6)
- repos: top2vec, bertopic


### paraphrase mining
- task of *finding paraphrases in large corpus of sentences*
- better for larger collections than using brute-force approach to score and rank all pairs


### translated sentence mining
#### marging based mining
[1812.10464.pdf (arxiv.org)](https://arxiv.org/pdf/1812.10464.pdf)
- to find translated sentences in two datasets:
	1. encode all sentences to respective embedding
	2. find k-nn sentences for all sentences in both directions (k typically between 4 and 16)
	3. score all possible sentence combinations using formula in 4.3
	4. pairs with highest scores are most likely translated sentences
		- find some cut-off where you ignore pairs below threshold; for high quality, threshold of ~1.2-1.3 is pretty good


### cross-encoders
#### bi-encoder vs cross-encoder
- **bi-encoders** - produce for a given sentence a sentence embedding. pass to a BERT independently sentences A and B, which result in sentence embeddings u and v. sentences are compared using cosine similarity
- **cross-encoders** - pass both sentences simultaneously to transformer network. produces output value between 0 and 1 indicating similarity of input sentence pair
	- does not produce sentence embedding
	- not able to pass individual sentences to cross-encoder
- cross-encoders achieve better performances than bi-encoders
	- but for many applications, not practical because they don't produce embeddings
	- also don't scale as well for large datasets

![[biencoder-vs-crossencoder.png]]

*when to use cross/bi-encoders?*
- cross-encoders: when you have a pre-defined set of sentence pairs you want to score
- bi-encoders: when you need a sentence embedding in vector space for efficient comparison
	- ex: information retrieval/semantic search, clustering


### image search
- sentence transformers provides models that allow you to embed images and text into same vector space, which allows you to find similar images and implement **image search**
- ex: CLIP model for text-to-image, image-to-text, image-to-image, text-to-text search