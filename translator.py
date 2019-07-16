from utils.alphabet import alphabet, letters
import re


class translator():

    def letter_translate(self, letter):
        """Translates the letter given in Gujarati and prints out the english pronounciation"""
        return list(letters.keys())[list(letters.values()).index(letter)]

    def translate(self, word):
        """Translates the word given in Gujarati and prints out the pronounciation in English"""
        word = re.sub(r'્', r'', word)
        word = [letter for letter in word]
        a = [list(alphabet.keys())[list(alphabet.values()).index(letter)] for letter in word]
        translation = ''.join(letter for letter in a)
        return translation
