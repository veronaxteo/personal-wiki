# cs 288 - natural language processing
# lecture notes from spring 2022
## introduction
- goal: deep understanding
	- requires knowledge, context, and grounding; just starting to see successes
- reality: shallow matching
	- requires robustness and scale; amazing successes, but fundamental limitations

transforming language
**speech systems**         
- **automatic speech recognition (ASR)** - audio in, text out
- **text to speech (TTS)** - text in, audio out

### related areas
- **computational linguistics** - using computational methods to learn more about how language works
- **cognitive science** - figuring out how human brain works, includes bits that do language
	- humans are the only working NLP prototype
- **speech processing** - mapping audio signals to text
	- traditionally separate from nlp, converging


## language models
### noisy channel model: ASR
- we want to predict a sentence given acoustics


### n-gram models
- use chain rule to generate worlds left-to-right
- can't condition atomically on the entire left context
- n-gram models make a markov assumption