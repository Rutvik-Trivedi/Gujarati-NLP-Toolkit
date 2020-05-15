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
        return text

    def remove_tek(self, text, tek_string):
        if str(type(tek_string))=="<class 'NoneType'>" or not tek_string:
            raise TypeError('tek_string needs to be a valid string')
        if str(type(text))=="<class 'list'>":
            for i in range(len(text)):
                text[i] = text[i].strip(tek_string)
        elif str(type(text))=="<class 'str'>":
            text = text.strip(tek_string)
        else:
            raise TypeError("Argument 'text' must be either a str or list")
        return text

    def poetic_preprocessing(self, text, remove_tek=False, tek_string=None):
        '''This function is only required when dealing with poetic corpora. Make sure to use this function along with the compulsory preprocessing to have decently accurate results with poetic corpora'''
        text = re.sub(r'।','.',text)
        text = re.sub(' ।।[૧૨૩૪૫૬૭૮૯૦]।।', '.', text)
        if remove_tek:
            text = self.remove_tek(text, tek_string)
        tokens = WordTokenizer(text, keep_punctuations=False)
        # Remove poetic words
        for i in range(len(tokens)):
            try:
                if tokens[i] in ['જી', 'રે', 'હો', 'હોજી', 'લોલ​', 'હે', 'હેજી', '...', 'સંતો']:
                    del(tokens[i])
            except:
                pass

        for i in range(len(tokens)):
            # Rule 1
            if tokens[i].endswith('જી'):
                tokens[i] = tokens[i].strip('જી')
            # Rule 2
            if tokens[i].endswith('ૈ'):
                tokens[i] = tokens[i].strip('ૈ')+'ે'
            # Rule 3
            index = tokens[i].find('ર')
            if tokens[i][index-1]=='િ' and index!=len(tokens[i])-1:
                tokens[i] = re.sub('િર', 'ૃ', tokens[i])

        return ' '.join(tokens)
