from tokenizer import SentenceTokenizer
from utils.stopwords import stopwords
from preprocessing import Preprocessor

import re

# You may need to add/remove suffixes/prefixes according to the corpora
suffixes = ['નાં','ના','ની','નો','નું','ને','થી','માં','એ','ઓ','ે','તા','તી','વા','મા','વું','વુ','ો','માંથી','શો','ીશ','ીશું','શે',
			'તો','તું','તાં','્યો','યો','યાં','્યું','યું','્યા','યા','્યાં','સ્વી','રે','ં','મ્','મ્','ી','કો']
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
		try:
			del(self.suffixes[self.suffixes.index(suffix)])
		except IndexError:
			print('{} not present in suffixes'.format(suffix))

	def delete_prefix(self, prefix):
		try:
			del(self.prefixes[self.prefixes.index(prefix)])
		except IndexError:
			print("{} not present in prefixes".format(prefix))


	def stem_word(self, sentence):
		word_list = sentence.strip('\u200b').split(' ')
		if not word_list[-1]:
			del(word_list[-1])
		return_list = []
		puctuations = ('.',',','!','?','"',"'",'%','#','@','&','…')
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


	def stem(self, text, poetic_preprocessing=False, remove_tek=False, tek_string=None):
		preprocessor = Preprocessor()
		text = preprocessor.compulsory_preprocessing(text)
		if poetic_preprocessing:
			text = preprocessor.poetic_preprocessing(text, remove_tek=remove_tek, tek_string=tek_string)
		l = SentenceTokenizer(text)
		if len(l)==1:
			sentence = l[0]
			return self.stem_word(sentence)
		else:
			a = []
			for sentence in l:
				a.append(self.stem(sentence))
			return a
