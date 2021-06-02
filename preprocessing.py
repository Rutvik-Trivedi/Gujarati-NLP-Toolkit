import re
from tokenizer import WordTokenizer

class Preprocessor():
    def __init__(self):
        self.suffixes = []
        pass

    def compulsory_preprocessing(self, text):
        '''This is a function to preprocess the text and make the necessary changes which are compulsory for any type of Gujarati NLP task'''
        text = re.sub(r'\u200b', '', text)
        text = re.sub(r'\ufeff', "", text)
        text = re.sub(r'…', " ", text)
        text = re.sub(r'  ', ' ', text)
        text = re.sub(r'”“', '', text)
        text = WordTokenizer(text)
        for i in range(len(text)):
            text[i] = text[i].rstrip(':')
        return ' '.join(text)

    def remove_tek(self, text, tek_string):
        '''
        Tek is the Gujarati word for the initial line of the poem. Whenever, one stanza of any poem is sung, the initial line of the poem is sung once again before starting the
        next stanza. This is called as singing a "Tek". Written poems mention the tek string too many a times. This will cause a problem of redundancy. Hence, removing it is
        necessary.
        '''
        if str(type(tek_string))=="<class 'NoneType'>" or not tek_string:
            raise TypeError('tek_string needs to be a valid string')
        if str(type(text))=="<class 'list'>":
            for i in range(len(text)):
                text[i] = text[i].rstrip(tek_string)
        elif str(type(text))=="<class 'str'>":
            text = text.rstrip(tek_string)
        else:
            raise TypeError("Argument 'text' must be either a str or list")
        return text

    def poetic_preprocessing(self, text, remove_tek=False, tek_string=None):
        '''This function is only required when dealing with poetic corpora. Make sure to use this function along with the compulsory preprocessing to have decently accurate results with poetic corpora'''
        text = re.sub(r'।','.',text)
        text = re.sub(' ।।[૧૨૩૪૫૬૭૮૯૦]।।', '.', text)
        if remove_tek:
            text = self.remove_tek(text, tek_string)
        tokens = WordTokenizer(text, corpus='poetry', keep_punctuations=False)

        for i in range(len(tokens)):
            # Rule 1
            if tokens[i].endswith('જી'):
                tokens[i] = tokens[i].strip('જી')
            # Rule 2
            if tokens[i].endswith('ૈ'):
                tokens[i] = tokens[i].strip('ૈ')+'ે'
            # Rule 3
            index = tokens[i].find('ર')
            if index == -1:
                pass
            elif index<len(tokens[i])-1 and tokens[i][index-1]=='િ':
                tokens[i] = re.sub('િર', 'ૃ', tokens[i])

        return ' '.join(tokens)
