from collections import defaultdict
import numpy as np
import pandas as pd
import pickle
import re

import sklearn_crfsuite
import sklearn
from sklearn_crfsuite import scorers
from sklearn_crfsuite import metrics
from sklearn.metrics import make_scorer
from sklearn.model_selection import RandomizedSearchCV
import scipy.stats



#TODO: Fix the Evaluation functions and improve the POS Tagger further.



class posTagger():

	def __init__(self, model='guj'):
		if not model.endswith('.rtm'):
			self.model_ = model+'.rtm'
		else:
			self.model_ = model

	def add_feature(self, features, feature_list, feature_name = None, func = None, **kwargs):
		if feature_name == None:
			raise ValueError("Argument 'feature_name' cannot be NoneType")
		if type(feature_name)!="<class 'str'>":
			raise TypeError("Argument 'feature_name' cannot be a "+ str(type(feature_name)))
		try:
			features[feature_name] = func(sentence, **kwargs)
			feature_list.append[feature_name]
			num_features = len(feature_list)
			return (num_features, features, feature_list)
		except Exception as e:
			print(str(e))
			return False

	def delete_feature(self, features, feature_list, feature_name=None):
		if feature_name == None:
			raise ValueError("Argument 'feature_name' cannot be NoneType")
		if type(feature_name)!="<class 'str'>":
			raise TypeError("Argument 'feature_name' cannot be a "+ str(type(feature_name)))
		try:
			del(features[feature_name])
			del(feature_list[feature_list.index(feature_name)])
			num_features = len(feature_list)
			return (num_features, features, feature_list)
		except Exception as e:
			print(str(e))
			return False

	def word2feature(self, sent, i):
		sent = sent.strip(' ').split(" ")
		word_n_tags = []
		for word in sent:
			try:
				word_n_tags.append([word.split('\\')[0], word.split('\\')[1]])
			except:
		 		pass
		try:
			word = word_n_tags[i][0]
			postag = word_n_tags[i][1]
			features = {
			'bias': 1.0,
			'word[-4:]': word[-4:],
			'word[-3:]': word[-3:],
			'word[:3]':word[:3],
			'word[:4]':word[:4],
			'word.isdigit()': word.isdigit(),
			}

			if i > 0:
				word1 = word_n_tags[i-1][0]
				postag1 = word_n_tags[i-1][1]
				features.update({
				'-1:word.isdigit()': word1.isdigit(),
				'-1:word[-3:]':word1[-3:],
				'-1:word[-4:]':word1[-4:],
				'-1:word[:3]':word1[:3],
				'-1:word[:4]':word1[:4],
				'-1:postag': postag1,
				'-1:postag[-3:]': postag1[-3:]
				})
			else:
				features['BOS'] = True

			if i < len(word_n_tags)-1:
				word1 = word_n_tags[i+1][0]
				postag1 = word_n_tags[i+1][1]
				features.update({
				'+1:word.isdigit()':word1.isdigit(),
				'+1:word[-3:]':word1[-3:],
				'+1:word[-4:]':word1[-4:],
				'+1:word[:3]':word1[:3],
				'+1:word[:4]':word1[:4],
				'+1:postag': postag1,
				'+1:postag[-3:]': postag1[-3:],
				})
			else:
				features['EOS'] = True

		except:
			features=None

		return features

	def sent2features(self, sent):
		sentence = sent.strip(' ').split()
		sent_to_features = []
		for i in range(len(sentence)):
			a = self.word2feature(sent,i)
			if a!=None:
				sent_to_features.append(a)
		return sent_to_features

	def sent2tokens(self, sent):
		sent = sent.strip(' ').split(' ')
		sent_to_tokens = []
		for word in sent:
			try:
				sent_to_tokens.append(word.split('\\')[0])
			except IndexError:
				pass
		return sent_to_tokens


	def sent2tags(self, sent):
		sent = sent.strip(' ').split(' ')
		return_list = []
		for word in sent:
			try:
				return_list.append(word.split('\\')[1])
			except IndexError:
				pass
		return return_list


	def read_text_from_corpus(self, path_to_corpus):
		data = pd.read_csv(path_to_corpus)
		list_sents = data["Value"].tolist()
		return list_sents

	def data_from_corpus(self, path_to_corpus):
		list_sents = self.read_text_from_corpus(path_to_corpus)
		train_X = [self.sent2features(sentence) for sentence in list_sents]
		train_y = [self.sent2tags(sentence) for sentence in list_sents]
		return (train_X, train_y)

	def train(self, train_X, train_y, algorithm='lbfgs', c1=0.1, c2=0.1, max_iterations=100, all_possible_transitions=True, save=False):
		if save==True and self.model_=='guj.rtm':
			raise ValueError("Model name must be given as an argument to the posTagger() constructor.")
		crf = sklearn_crfsuite.CRF(
			algorithm=algorithm,
			c1=c1,
			c2=c2,
			max_iterations=max_iterations,
			all_possible_transitions=all_possible_transitions
			)
		crf.fit(train_X, train_y)

		if save:
			with open(self.model_, "wb") as f:
				pickle.dump(crf,f)

	def evaluate(self, test_X, test_y, metric='flat_f1_score', average='weighted', digits=3):
		if self.model_==None:
			raise ValueError("Model can not be NoneType. Load an existing model or create a new one and pass as a parameter")
		with open(self.model_, 'rb') as f:
			crf = pickle.load(f)
		labels = list(crf.classes_)
		pred_y = crf.predict(test_X)
		if metric == 'flat_f1_score':
			flat_f1_score = metrics.flat_f1_score(test_y, pred_y, average=average, labels=labels)
			print(flat_f1_score)

		if metric=='flat_classification_report':
			sorted_labels = sorted(labels)
			print(metrics.flat_classification_report(
				test_y, pred_y, labels=sorted_labels, digits=digits
				))

	def load(self):
		try:
			with open(self.model_, 'rb') as f:
				crf = pickle.load(f)
		except FileNotFoundError:
			raise FileNotFoundError('Specified model could not be found. Please make sure it is within the working directory or you have mentioned the path to the file.')

		return crf

	def predict(self, test_X):
		if self.model_==None:
			raise ValueError('Model can not be NoneType. Load an existing model or train a new one and pass it as a parameter')
		with open(self.model_,"rb") as f:
			crf = pickle.load(f)
		pred_y = crf.predict(test_X)
		return pred_y

	def optimize_hyperparameters(self, train_X, train_y, metric='flat_f1_score', average='weighted', cv=3, verbose=1, n_jobs=-1, n_iter=50):
		params_space = {
		'c1': scipy.stats.expon(scale=0.5),
		'c2': scipy.stats.expon(scale=0.05)
		}

		with open(self.model_,'rb') as f:
			model = pickle.load(f)

		labels = list(model.classes_)

		if metric=='flat_f1_score':
			scorer = make_scorer(metrics.flat_f1_score, average=average, labels=labels)
			rs = RandomizedSearchCV(model, params_space,
                        cv=cv,
                        verbose=verbose,
                        n_jobs=n_jobs,
                        n_iter=n_iter,
                        scoring=scorer)
			rs.fit(train_X, train_y)
			return rs
		else:
			print("Optimization currently unavailable for the given metric")
			return None

	def sentence_to_features(self, sentence):
		punctuations = ['.',',','"',"'","!",'?','<','>','/','&',"%","#",'@','-','+','*','(',")"]
		sent = sentence.strip(' ').split()
		sentence_features = []
		for word,i in zip(sent, range(len(sent))):
			features = {
			'bias': 1.0,
			'word[-4:]': word[-4:],
			'word[-3:]': word[-3:],
			'word[:3]':word[:3],
			'word[:4]':word[:4],
			'word.isdigit()': word.isdigit(),
			}
			if i > 0:
				word1 = sent[i-1]
				features.update({
				'-1:word.isdigit()': word1.isdigit(),
				'-1:word[-3:]':word1[-3:],
				'-1:word[-4:]':word1[-4:],
				'-1:word[:3]':word1[:3],
				'-1:word[:4]':word1[:4]})
				if word1 in punctuations:
					features.update({
					'-1:postag': 'RD_PUNC',
					'-1:postag[-3:]': 'UNC'})
			else:
				features['BOS'] = True
			if i < len(sent)-1:
				word1 = sent[i+1]
				features.update({
				'+1:word.isdigit()': word1.isdigit(),
				'+1:word[-3:]':word1[-3:],
				'+1:word[-4:]':word1[-4:],
				'+1:word[:3]':word1[:3],
				'+1:word[:4]':word1[:4],})
				if word1 in punctuations:
					features.update({
					'+1:postag': 'RD_PUNC',
					'+1:postag[-3:]': 'UNC'})
			else:
				features['EOS'] = True
			sentence_features.append(features)
		return sentence_features


	def pos_tag(self, sent):
		sent = re.sub(r'([.,\'\\"!?%#@*<>\+\-\(\)])', r' \1', sent)
		sent = re.sub(r'\u200b', r'', sent)
		sentence = sent
		sent = self.sentence_to_features(sent)
		y = self.predict([sent])
		return_list = []
		for word, tag in zip(sentence.split(), y[0]):
			return_list.append((word, tag))
		return return_list



if __name__ == '__main__':
	tagger = posTagger()
	#X,y = tagger.data_from_corpus('guj_pos_tag.txt')
	# train_X = X[:int(0.8*len(X))]
	# train_y = y[:int(0.8*len(y))]
	# test_X = X[int(0.8*len(X)):]
	# test_y = y[int(0.8*len(y)):]
	# tagger.train(train_X, train_y, save=False)
	#rs = tagger.optimize_hyperparameters(train_X, train_y)
	#print(rs)
	#tagger.evaluate(test_X, test_y)

	sentence = 'તારુ નામ શુ છે?'
	print(tagger.pos_tag(sentence))
