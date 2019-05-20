from utils import stopwords

suffixes = ['નાં','ના','ની','નો','નું','ને','થી','માં','એ','ઓ','ે']


def stemmer(word, lemmatize=False):
	
	if word in stopwords:
		return word
	

	if not lemmatize:
		for i in suffixes:
			if word.endswith(i):
				word.strip(i)
		return word
	

	else:
		#Lemmatize and
		return word
