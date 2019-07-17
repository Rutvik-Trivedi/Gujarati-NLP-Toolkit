from tokenizer import SentenceTokenizer
from utils.stopwords import stopwords


import re

suffixes = ['નાં','ના','ની','નો','નું','ને','થી','માં','એ','ઓ','ે','તા','તી','વા','મા','વું','વુ','ો','માંથી','શો','ીશ','ીશું','શે',
			'તો','તું','તાં','્યો','યો','યાં','્યું','યું','્યા','યા','્યાં','સ્વી']
prefixes = ['અ']



class Stemmer():
	def __init__(self):
		self.suffixes = suffixes
		self.prefixes = prefixes

	def add_suffix(self, suffix):
		self.suffixes.append(suffix)

	def add_prefix(self, prefix):
		self.prefixes.append(prefix)

	def delete_suffix(self, suffix):
		del(self.suffixes[self.suffixes.index(suffix)])

	def delete_prefix(self, prefix):
		del(self.prefixes[self.prefixes.index(prefix)])

	def _remove_junk(self, text):
		text = re.sub(r'\u200b', '', text)
		return text

	def stem_word(self, sentence):
		word_list = sentence.strip('\u200b').split(' ')
		if not word_list[-1]:
			del(word_list[-1])
		return_list = []
		puctuations = ('.',',','!','?','"',"'",'%','#','@','&')
		for word in word_list:
			a = word
			if word.endswith(puctuations):
				a = word[:-1]
			if a in stopwords:
				return_list.append(a)
				continue
			for suffix in suffixes:
				if a.endswith(suffix):
					a = a.rstrip(suffix)
					break
			for prefix in prefixes:
				if a.startswith(prefix):
					a = a.lstrip(prefix)
					break
			if word.endswith(puctuations):
				a+=str(word[-1])
			return_list.append(a)
		return_sentence = " ".join(return_list)
		return return_sentence


	def stem(self, text):
		text = self._remove_junk(text)
		l = SentenceTokenizer(text)
		if len(l)==1:
			sentence = l[0]
			return self.stem_word(sentence)
		else:
			a = []
			for sentence in l:
				a.append(self.stem(sentence))
			return a
