
# Gujarati-NLP-Toolkit
A Python NLP Toolkit for Gujarati(Under Progress) created on top of Scikit-Learn for NLP of Gujarati Language.


## Added Features:

1) POS Tagger:

	a) Implementation:
	```python
	import posTagger as pt
	tagger = pt.posTagger()
	sentence = 'તારુ નામ શુ છે?'  # What is your name?
	print(tagger.pos_tag(sentence))   # [('તારુ', 'PR_PRP'), ('નામ', 'N_NN'), ('શુ', 'N_NN'), ('છે', 'V_VAUX'), ('?', 'RD_PUNC')]
	```

	b) Training your own posTagger:
	```python
	import posTagger as pt
	tagger = pt.posTagger('model_name')   # Give any name for your model
	train_X, train_y = tagger.data_from_corpus('path/to/corpus/')
	```
	
	Your corpus must be in txt(comma delimited) or csv format and must contain a column 'Value' having the data in the form:
	```
	Row1:    'word1\tag1 word2\tag2 word3\tag3 ....... wordn\tagn'
	Row2:    'word1\tag1 word2\tag2 word3\tag3 ....... wordn\tagn'
	```
	Else You may create your own train_X, train_y of the form:
	```
	train_X:  [[feature_dict of word1, feature_dict of word2, ........ , feature_dict of wordn],     //Sentence 1
		      [feature_dict of word1, feature_dict of word2, ........ , feature_dict of wordn]]	   // Sentence n
	train_y:  [[tags of sentence 1], [tags of sentence 2], ........, [tags of sentence n]]
	```
	```python
	tagger.train(train_X, train_y, save=True)    # save = False if you don't want to save the model	
	```
	
	c)  Loading your trained posTag Model:
	```python
	import posTagger as pt
	tagger = posTagger('model_name')
	model = tagger.load()
	## Carry out your processes
	```

	d) Evaluation Processes:
	This feature is under development. Please check again later.

# TODO:
- Improving the POS Tagger which currently overfits due to fewer data. Improve implementation.
- Fix Bugs in the evaluation of POS Tagger.

