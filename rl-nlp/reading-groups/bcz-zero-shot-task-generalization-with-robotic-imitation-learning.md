# BC-Z: zero-shot task generalization with robotic imitation learning

**goal**: learn *semantic latent space* for prompting/goals
- ex: "move the block", "lift the block"
- after these, when robot sees "move the star," hopefully it has some idea of what to do because it's already seen "move"
	- question is how we adjust for "star"

**idea**: align/ground latent space using natural language

BC-Z - behavioral cloning, latent


## architecture
[[bcz-network-architecture.png]]
- training; giving robots various tasks
- zero-shot test - hasn't seen tasks during training

BC-Z
- **goal**: align *offline dataset* of interactions semantically with their task
- encoder takes in visuals or text
	- for language, they freeze the encoder
	- for video, during train time, they optimize it end-to-end
		- end-to-end optimized resnet 18 encoder with paired human data
			- "human data": for example if you want robot to "put banana in purple bowl," have a human do that, and then encode that video in the encoder
		- enforcing consistency between domains through *language regression loss*
			- implicitly also train video encoder to predict language embeddings
			
- policy
	- behavioral cloning
	- regress actions with *huber loss*

- some learning hacks:
	1. open loop supervision --> train: predict 10 actions, test: execute first action
	2. n-step actions --> predict change across n timesteps

## dataset collection
[[bcz-train-and-unseen-tasks.png]]
- entirely real world deployment --> 6-15 randomized objects, 100 tasks, 9 skills

- **problem**: collect diverse data at scale, provide corrective feedback during training
- HG-DAgger - manually label encountered OOD data during during traing time
	1. full expert control (initial dataset)
	2. "shared autonomy" --> iteratively deploy updated policy with expert intervention


## experimental setup
- **train**: DAgger dataset
	- 2 disjoint object datasets:
		a) 21 different tasks (wide range of skills)
		b) 79 different tasks (small range of skills, more objects)
	- train on both datasets
	- sets/combinations of the datasets

- **zero/few shot test**:
	- novel sentences, averages of several videos of new tasks
	- cross-object set (i.e. mix a + b settings) generalization via handout tasks


## results
- seems like language does pretty well, video not so much
- ablation studies (take away certain parts of something that does well and see what affects it)


## discussion
- advantages of language over video? video over language? limitations of both?
	- language is easier to specify
- what else can we provide language supervision for?
	- human-in-the-loop with language?
	- reward specification with language?
- CLIP embeddings? how can we extend to these?