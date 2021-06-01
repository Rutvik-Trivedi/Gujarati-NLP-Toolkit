from utils.stopwords import prose_stopwords, poetry_stopwords
import re

def WordTokenizer(data, corpus='poetry', keep_punctuations=True, keep_stopwords = True):
    if not keep_punctuations:
        data = re.sub(r'[.?/,:;*\"!$#@%^&~\(\)]','',data)

    data = re.sub(r'([.,\'\\"!?%#@*<>|\+\-\(\)])', r' \1', data)
    data = re.sub(r'[।।(૧૨૩૪૫૬૭૮૯)*।।]', '  ', data)
    data = re.sub(r"   ", '', data)
    data = re.sub(r'…', " ", data)
    data = re.split(r'[ -]',data)
    return_list = []
    if not keep_stopwords and corpus=='poetry':
        a = []
        for word in data:
        	if word not in poetry_stopwords:
        		a.append(word)
        return a

    if not keep_stopwords and corpus=='prose':
        a = []
        for word in data:
        	if word not in prose_stopwords:
        		a.append(word)
        return a


    for i in data:
        if i:
            return_list.append(i)
            

    return return_list


def SentenceTokenizer(data):
    data = data.strip()
    data = re.sub(r'([.!?])', r'\1 ', data)
    data = re.split(r'  ',data)
    if not data[-1]:
    	del(data[-1])
    return data
