from utils.alphabet import alphabet, letters, utfalpha, punctuations
from utils.gujarati_hindi import gu_hi, hi_gu
import re


class Transliterator():

    def __init__(self, verbose=False):
        self.verbose=verbose

    def letter_transliterate_gujarati_to_english(self, letter):
        """Transliterates the letter given in Gujarati and prints out the english pronounciation"""
        return list(letters.keys())[list(letters.values()).index(letter)]

    def gujarati_to_english(self, word):
        """Transliterates the word given in Gujarati and prints out the pronounciation in English"""
        word = re.sub(r'્', r'', word)
        word = re.sub(r'\u200b',r'',word)
        return_list = []
        for i in range(len(word)):
            try:
                if i<len(word)-1:
                    if word[i] == 'ં' and word[i+1] in punctuations.keys():
                        continue
                if i==len(word)-1 and word[i]=='ં':
                    continue
                a = list(alphabet.keys())[list(alphabet.values()).index(word[i])]
                return_list.append(a)
            except ValueError:
                x = word[i].encode('utf-8')
                a = list(utfalpha.keys())[list(utfalpha.values()).index(x)]
                return_list.append(a)
        translation = ''.join(letter for letter in return_list)
        return translation

    def hindi_to_gujarati(self, sentence):
        """Transliterates the sentence given in Hindi and prints out the pronounciation in Gujarati"""
        l = list(sentence)
        for i in range(len(l)):
            try:
                l[i] = hi_gu[l[i]]
            except KeyError:
                if self.verbose:
                    print("Warning: {} does not exist in the dictionary".format(l[i]))
                pass
        l = ''.join(l)
        l = re.sub(r'\u200b', "", l)
        l = re.sub(r'\u200d', "", l)
        return l

    def gujarati_to_hindi(self, sentence):
        """Transliterates the word given in Gujarati and prints out the pronounciation in Hindi"""
        l = list(sentence)
        for i in range(len(l)):
            try:
                l[i] = gu_hi[l[i]]
            except:
                if self.verbose:
                    print("Warning: {} does not exist in the dictionary".format(l[i]))
                pass
        return ''.join(l)
