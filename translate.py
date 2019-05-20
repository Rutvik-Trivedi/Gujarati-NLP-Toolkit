from utils import alphabet


class translate():

    def __init__(self,letter=None,word=None):
        self.letter = letter
        self.word = word

    def letter_translate(self, letter, output=True):
        """Translates the letter given in Gujarati and prints out the english pronounciation"""
        self.letter = letter
        if output:
            print(list(alphabet.keys())[list(alphabet.values()).index(letter)])
        return list(alphabet.keys())[list(alphabet.values()).index(letter)]

    def word_translate(self, word, output=True):
        """Translates the word given in Gujarati and prints out the pronounciation in English"""
        self.word = word
        word = [letter for letter in word]
        a = [list(alphabet.keys())[list(alphabet.values()).index(letter)] for letter in word]
        translation = ''.join(letter for letter in a)
        if output:
            print(translation)
        return translation
