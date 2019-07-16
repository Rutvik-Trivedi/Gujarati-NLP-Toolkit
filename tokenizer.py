from utils.stopwords import stopwords
import re

def WordTokenizer(data, keep_punctuations=True, keep_stopwords = True):
    if not keep_punctuations:
        data = re.sub(r'[.?/,:;*\"!$#@%^&~\(\)]','',data)

    data = re.sub(r'([.,\'\\"!?%#@*<>\+\-\(\)])', r' \1', data)
    data = re.split(r'[ -]',data)
    if not keep_stopwords:
        a = []
        for word in data:
        	print(word)
        	if word not in stopwords:
        		a.append(word)
        return a
    
    return data


def SentenceTokenizer(data, tokenize_by_comma = False):
    data = data.strip()
    if tokenize_by_comma:
        data = re.split(r'[,.?!]',data)
    else:
        data = re.split(r'[.?!]',data)
    if not data[-1]:
    	del(data[-1])
    return data
