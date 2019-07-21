from utils.alphabet import alphabet, letters, utfalpha, punctuations
import re


class translator():

    def letter_translate(self, letter):
        """Translates the letter given in Gujarati and prints out the english pronounciation"""
        return list(letters.keys())[list(letters.values()).index(letter)]

    def translate(self, word):
        """Translates the word given in Gujarati and prints out the pronounciation in English"""
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

if __name__=='__main__':
    translator = translator()
    # for a in alphabet:
    #     print(a)
    print(translator.translate("અરે યાર શુ કરે છેં"))
    # print('આ'.encode('utf-8'))
    # string = b'\xe0\xaa\x91'.decode('utf-8')
    # print(string)