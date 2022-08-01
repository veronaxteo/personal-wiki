# chapter 3 - n-grams

## key concepts & words
language model, n-gram, maximum likelihood estimate, perplexity, smoothing, backoff, interpolation, discounting, kneser-ney, continuation

## summary
- language models offer a way to assign a probability to a sentence or other sequence of words, and to predict a word from preceding words
	- n-grams are markov models that estimate words from a fixed window of previous words; probabilities can be estimated by counting in corpus and normalizing (MLE)
	- n-gram language models are evaluated extrinsically in some tasks, or intrinsically using perplexity
	- perplexity of test set is the geometric mean of inverse test set probability computed by model
	- smoothing algorithms provide more sophisticated way to estimate probability of n-grams. common algorithms rely on lower-order n-gram counts through backoff or interpolation
	- both backoff and interpolation require discounting to create a probability distribution
	- kneser-ney smoothing makes use of probability of a word being a novel continuation. mixes discounted probability with lower-order continuation probability


*from wikipedia:*

> an **n-gram** (or **Q-gram**) is a contiguous sequence of n items from a given sample of text or speech.
> 
> two benefits of n-gram models: simplicity and scalability


- we want to assign probabilities to sentences
	- speech recognition, machine translation, augmentative and alternative communication systems (AAC)
- **language models (LMs)** - models that assign probabilities to sequences of words
- **n-gram** - a sequence of n words/
	- simplest model that assigns probabilities to sentences and sequences of words
	- "n-gram" can mean either the word sequence itself or the predictive model that assigns it a probability


## n-grams
- if we want to compute $P(w|h)$, probability of a word given history h, we could take a very large corpus and count the number of times we see history followed by the word
	- but even web isn't big enough for good estimates because *language is creative*

- intuition: instead of computing the probability of a word given its entire history, we can approximate the history by just the last few words

- **bigram** model - approximates probability of a word given all previous words by using only conditional probability of preceding word
	- $P(w_n|w_{1:n-1}) \approx P(w_n|w_{n-1})$

- **Markov** assumption - assumption that probability of a word depends only on the previous word
- Markov models are class of probabilistic models that assume we can predict probability of some future unit without looking too far into past

- we can generalize bigram to the trigram and thus to the **n-gram**, which looks n-1 words into past
	- $P(w_n|w_{1:n-1}) \approx P(w_n|w_{n-N+1:n-1})$


#### how we do estimate these n-gram probabilities?
- **maximum likelihood estimation (MLE)** - get MLE estimate for parameters of an n-gram model by getting counts from a corpus and **normalizing** the counts so that they lie between 0 and 1

general case of MLE n-gram parameter estimation:

$P(w_n|w_{1:n-1}) \approx P(w_n|w_{n-N+1:n-1}) = \dfrac {C(w_{n-N+1:n-1} w_n)}{C(w_{n-N+1:n-1})}$ 
where $C(w_{n-1}w_n)$ is the count of the bigram


- **relative frequency** - dividing observed frequency of particular sequence by observed frequency of a prefix


#### some practical issues:
- for larger n-grams (4-grams, 5-grams), need to assume extra context to left and right of sentence end
- always represent and compute language model probabilities in log format as **log probabilities**
	- since probabilities are <= 1, the more probabilities we multiple together, the smaller the product becomes --> potential numerical underflow
	- log probabilities allows us to get numbers that are not as small


## evaluating language models
- **extrinsic evaluation** - end-to-end evaluation in which you embed language model in an application and measure how much the application improves
	- often very expensive

- **intrinsic evaluation** - measures quality of model independent of any application
	- need training and test set
	- development test set or devset; when we use a test set so often, we may implicitly tune to it, so need fresh test set
	- usually 80% training, 10% development, 10% test


### perplexity
- **perplexity (PP)** - perplexity of language model on a test set is the *inverse probability of the test set, normalized by number of words*
	- high conditional probability of word sequence = lower perplexity
	- thus, minimizing perplexity == maximizing test set probability

- another way to think about perplexity is that it's the *weighted average branching factor* of a language
	- branching factor of a language = number of possible next words that can follow any word

- closely related to information-theoretic notion of entropy
- the more information the n-gram gives us about the word sequence, the lower the perplexity

- an intrinsic improvement in perplexity does not guarantee an extrinsic improvement in performance of a language processing task
	- perplexity as a quick check


## sampling sentences from a language model
- **sampling** from a distribution means to choose random points according to their likelihood
- more likely to generate sentences that model thinks have high probability


## generalization and zeros
- probabilities often encode specific facts about given training corpus and n-grams do better job of modeling training corpus as we increase n
- the longer the context for training, the more coherent the sentences
- use training corpus that has a similar genre to task we are trying to accomplish, as well as appropriate dialect or variety

### some problems
- **sparsity**, **zeros** (things that don't occur in training set but do in test set)

- **closed vocabulary** - know all words that can occur, no unknown words
- **out of vocabulary (OOV)** words - words we haven't seen before; % of OOV words in test set is called the *OOV rate*
- **open vocabulary** system - model potential unknown words in test set by adding a pseudo-word called \<UNK\>


## smoothing
- motivation: we want to keep model from assigning 0 probability to unseen events (e.g. words in vocabulary but appear in test set in unseen context)
- **smoothing (discounting)** - decrease probability mass from some more frequent events and give it to events never seen

### laplace smoothing
- add one to all n-gram counts before normalizing them into probabilities
	- which is why it's also known as **add-one** smoothing
- does not perform well so not used in modern n-gram models, but gives useful baseline and is also practical for other tasks like text classification

$P_{Laplace}(w_n|w_{1:n-1}) = \dfrac {C(w_{n-1} w_n)+1}{C(w_{n-1})+ V}$ 

for V words in vocabulary


### add-k smoothing
- instead of adding 1 to each count, we add a fractional count $k$
- requires we have a method for choosing $k$, e.g. by optimizing on devset
- still doesn't work well for most tasks (okay for text classification)

$P_{Add-k}(w_n|w_{1:n-1}) = \dfrac {C(w_{n-1} w_n)+k}{C(w_{n-1})+kV}$


### back-off and interpolation
- sometimes, using less context is a good thing to help us generalize more for contexts that model has not learned much about
- **backoff** - use trigram if evidence is sufficient, otherwise bigram, otherwise unigram
	- only "back off" to lower-order n-gram if have 0 evidence for high-order n-gram

- **interpolation** - always mix probability estimates from all n-gram estimators, weighting and combining trigram, bigram, and unigram counts

- **katz backoff** - reply on discounted probability P* if seen this n-gram before; otherwise, recursively back off to katz probability for shorter-history (n-1)-gram
	- often combined with smoothing method called **good-turing**


## kneser-ney smoothing
- one of the most commonly used and best performing n-gram smoothing methods
- **absolute discounting** - subtract fixed/absolute discount $d$ from each count

- kneser-ney intuition: instead of $P(w)$ which answers the question "how likely is $w$?", we want a model $P_{continuation}$ that answers question "how likely is $w$ to appear as a novel continuation?"
	- base estimate of $P_{continuation}$ on the *number of different contexts word w has appeared in*

- equation for **interpolated kneser-ney** smoothing for bigrams:

$P_{KN}(w_i|w_{i-1})) = \dfrac{max(C(w_{i-1}w_i)-d,0)}{C(w_i-1)} + \lambda(w_{i-1})P_{continuation}(w_i)$


- best performing version of KN smoothing is called **modified kneser-ney** smoothing
	- instead of single fixed discount $d$, use 3 different discounts for n-grams with counts of 1, 2, and 3, respectively


## huge language models and stupid backoff
- efficiency considerations: store each word as 64-bit hash number instead of string, prune model, build approximate language models using techniques like **bloom filters**
- a simpler algorithm may be sufficient: **stupid backoff**
	- no discounting of higher-order probabilities; if higher-order n-gram has 0 count, simply backoff to lower order n-gram, weighed by a fixed weight


## perplexity's relation to entropy
- **entropy** - a measure of information
- one way of thinking about entropy is as a lower bound on number of bits it would take to encode a certain decision or piece of information in optimal coding scheme

- a stochastic process is **stationary** if the probabilities it assigns to a sequence are invariant with respect to shifts in the time index
	- natural language is not stationary

- **cross entropy**
	- an upper bound on entropy
	- perplexity of model on a sequence of words is $2^{cross-entropy}$ 