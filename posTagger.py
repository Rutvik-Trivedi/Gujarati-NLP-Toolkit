import pandas as pd
import numpy as np
import pickle
import re
import warnings
import os
warnings.filterwarnings('ignore')

from nltk.tag import CRFTagger

from preprocessing import Preprocessor
from tokenizer import WordTokenizer
from utils.alphabet import numbers, punctuations


class posTagger(CRFTagger):

	def __init__(self, model='guj', verbose=True, corpus='poetry', tek_string=None):
		super(posTagger, self).__init__(verbose=verbose)
		self._model_file = model.strip('.crf.pkl')+'.crf.pkl'
		self.tags = set()
		self.corpus=corpus
		self.tek_string = tek_string

	def eval(self):
		self.set_model_file(self._model_file)

	def rename_model(self, old_name, new_name):
		os.rename(old_name+'.pkl', new_name+'.pkl')
		return True


	# Override
	def _get_features(self, tokens, idx):
		numbs = numbers.values()
		puncts = punctuations.values()

		token = tokens[idx]
		feature_list = []

		if not token:
			return feature_list

		for number in numbs:
			if number in list(token):
				feature_list.append("HAS_NUM")

		for punctuation in puncts:
			if punctuation in list(token):
				feature_list.append("PUNCTUATION")

		feature_list.append("WORD_" + token)
		feature_list.append("LENGTH_" + str(len(token)))

		if len(token) > 1:
			feature_list.append("SUF_" + token[-1:])
			feature_list.append("PRE_" + token[:1])
		if len(token) > 2:
			feature_list.append("SUF_" + token[-2:])
			feature_list.append("PRE_" + token[:2])
		if len(token) > 3:
			feature_list.append("SUF_" + token[-3:])
			feature_list.append("PRE_" + token[:3])

		if idx >= 1:
			previous_token = tokens[idx-1]
			if not previous_token:
				return feature_list

			for number in numbs:
				if number in list(previous_token):
					feature_list.append("HAS_NUM")

			for punctuation in puncts:
				if punctuation in list(previous_token):
					feature_list.append("PUNCTUATION")

			if len(previous_token) > 1:
				feature_list.append("SUF_" + previous_token[-1:])
				feature_list.append("PRE_" + previous_token[:1])
			if len(previous_token) > 2:
				feature_list.append("SUF_" + previous_token[-2:])
				feature_list.append("PRE_" + previous_token[:2])
			if len(previous_token) > 3:
				feature_list.append("SUF_" + previous_token[-3:])
				feature_list.append("PRE_" + previous_token[:3])

			feature_list.append("PREV_WORD_" + previous_token)
			feature_list.append("PREV_LENGTH_" + str(len(previous_token)))

		if idx >= 2:
			previous_token = tokens[idx-2]
			if not previous_token:
				return feature_list

			for number in numbs:
				if number in list(previous_token):
					feature_list.append("HAS_NUM")

			for punctuation in puncts:
				if punctuation in list(previous_token):
					feature_list.append("PUNCTUATION")

			if len(previous_token) > 1:
				feature_list.append("SUF_" + previous_token[-1:])
				feature_list.append("PRE_" + previous_token[:1])
			if len(previous_token) > 2:
				feature_list.append("SUF_" + previous_token[-2:])
				feature_list.append("PRE_" + previous_token[:2])
			if len(previous_token) > 3:
				feature_list.append("SUF_" + previous_token[-3:])
				feature_list.append("PRE_" + previous_token[:3])

			feature_list.append("PREV_PREV_WORD_" + previous_token)
			feature_list.append("PREV_PREV_LENGTH_" + str(len(previous_token)))



		if idx < len(tokens)-1:
			next_token = tokens[idx+1]
			if not next_token:
				return feature_list

			for number in numbs:
				if number in list(next_token):
					feature_list.append("HAS_NUM")

			for punctuation in puncts:
				if punctuation in list(next_token):
					feature_list.append("PUNCTUATION")

			if len(next_token) > 1:
				feature_list.append("SUF_" + next_token[-1:])
				feature_list.append("PRE_" + next_token[:1])
			if len(next_token) > 2:
				feature_list.append("SUF_" + next_token[-2:])
				feature_list.append("PRE_" + next_token[:2])
			if len(next_token) > 3:
				feature_list.append("SUF_" + next_token[-3:])
				feature_list.append("PRE_" + next_token[:3])

			feature_list.append("NEXT_WORD_" + next_token)
			feature_list.append("NEXT_LENGTH_" + str(len(next_token)))

		if idx < len(tokens)-2:
			next_token = tokens[idx+2]
			if not next_token:
				return feature_list

			for number in numbs:
				if number in list(next_token):
					feature_list.append("HAS_NUM")

			for punctuation in puncts:
				if punctuation in list(next_token):
					feature_list.append("PUNCTUATION")

			if len(next_token) > 1:
				feature_list.append("SUF_" + next_token[-1:])
				feature_list.append("PRE_" + next_token[:1])
			if len(next_token) > 2:
				feature_list.append("SUF_" + next_token[-2:])
				feature_list.append("PRE_" + next_token[:2])
			if len(next_token) > 3:
				feature_list.append("SUF_" + next_token[-3:])
				feature_list.append("PRE_" + next_token[:3])

			feature_list.append("NEXT_NEXT_WORD_" + next_token)
			feature_list.append("NEXT_NEXT_LENGTH_" + str(len(next_token)))

		return feature_list



	def collect_train_data(self, file, sep='\t'):
		data = pd.read_csv(file, sep=sep)
		print(data.columns)
		data = data['Value']
		data = data.replace(np.nan, "", regex=True)
		data = data.replace(u'\ufeff', '', regex=True)
		data = data.tolist()
		return data

	def split_correctly(self, word):
		try:
			splitted = word.split('\\')
			splitted[1] = splitted[1].split('_')[1]
			if '-' in splitted[1]:
				splitted[1] = splitted[1].split('-')[1]
		except IndexError:
			pass
		if len(splitted)<2:
			return (splitted[0],"EMPTY")
		else:
			return tuple(splitted)

	def structure_data(self, file, sep='\t'):
		data = self.collect_train_data(file, sep=sep)

		train_data = []
		for i in range(len(data)):
			sent_list = []
			sentence = data[i].split(' ')

			for j in range(len(sentence)):
				sentence[j] = self.split_correctly(sentence[j])
				self.tags.add(sentence[j][1])

			train_data.append(sentence)

		return train_data

	def pos_tag(self, sentence, remove_tek=False):
		preprocessor = Preprocessor()
		sent = preprocessor.compulsory_preprocessing(sentence)

		if self.corpus=='poetry':
			sent = preprocessor.poetic_preprocessing(sent, remove_tek=remove_tek, tek_string=self.tek_string)
			sent = WordTokenizer(sent, keep_stopwords=False)


		elif self.corpus=='prose':
			sent = WordTokenizer(sent, keep_stopwords=True)


		else:
			raise ValueError("Corpus can not be {}".format(corpus))


		tags = self.tag(sent)
		return tags
