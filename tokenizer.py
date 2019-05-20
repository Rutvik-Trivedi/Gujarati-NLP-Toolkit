from utils import alphabet
from utils import advanced_tokenize_utils

import re

def WordTokenizer(data, keep_punctuations=False, keep_stopwords = True):
    if not keep_punctuations:
        data = re.sub(r'[.?/,:;*\"!$#@%^&~\(\)]','',data)
    data = re.split(r'[ -]',data)
    if not keep_stopwords:
        from utils import stopwords
        data = [words for words in data and words not in stopwords]
    return data


def SentenceTokenizer(data, tokenize_by_comma = False):
    data = data.strip()
    if tokenize_by_comma:
        data = re.split(r'[,.?!]',data)
    else:
        data = re.split(r'[.?!]',data)
    return data

def advanced_word_tokenize(data, keep_punctuations=False, keep_stopwords=True):
    if not keep_punctuations:
        data = re.sub(r'[.?/,:;*\"!$#@%^&~\(\)]','',data)
    data = re.split(r'[ -]',data)
    if not keep_stopwords:
        from utils import stopwords
        data = [words for words in data and words not in stopwords]
    return data
