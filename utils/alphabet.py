import re
from itertools import chain

###########################################################################################################
## --> Here the dictionaries for the vowels and consonants are provided for usage.                        #
## --> The dictionaries are designed in a way such that the keys will provide the english pronounciation  #
##     and the values will provide the corresponding alphabet                                             #
## --> The keys having pronounciations written in CAPS are to be pronounced more stressfully than the     #
##     ones with lowercase keys.                                                                          #
## --> The above point will be well understood by reading the comments in the file.                       #
###########################################################################################################



vowels = {'a':'અ',
          'aa':'આ',
          'y':'ઇ',   # Sometimes is also pronounced as 'i'
          'i':'ઇ',   # Sometimes is also pronounced as 'y' (as the 'y' in 'literally')
          'ee':'ઈ',
          'u':'ઉ',
          'oo':'ઊ',
          'ru':'ઋ',   # Sometimes is also pronounced as 'ri'
          'e':'એ',
          'ai':'ઐ',
          'o':'ઓ',
          'au':'ઔ',
          'am':'અં',  # Sometimes is also pronounced as 'an'
          'ah':'અઃ',
          'an':'અં'}  # Sometimes is also pronounced as 'am'

signs = {'aa':'ા',
         'i':'િ',
         'ee':'ી',
         'u':'ુ',
         'oo':'ૂ',
         'ru':'ૄ',
         'ri':'ૃ',
         'e':'ે',
         'ai':'ૈ',
         'o':'ો',
         'au':'ૌ',
         'an':'ં',
         'ah':'ઃ '}

velar_consonants = {'k':'ક્',   # Sometimes is also pronounced as 'c'
                    'c':'ક્',   # Sometimes is also pronounced as 'k'
                    'kh':'ખ્',
                    'g':'ગ્',
                    'gh':'ઘ્',
                    'ṅa':'ઙ'}

palatal_consonants = {'ch':'ચ્',
                      'chh':'છ્',
                      'j':'જ્',
                      'z':'ઝ્',    # Sometimes is also pronounced as 'jh'
                      'jh':'ઝ્',   # Sometimes is also pronounced as 'z'
                      'ña':'ઞ'}

retroflex_consonants = {'T':'ટ્',  #As the 't' in 'pot'
                        'Th':'ઠ્', # As the 'th' in 'thunder'
                        'D':'ડ્',  #As the 'd' in 'hand'
                        'Dh':'ઢ્',
                        'N':'ણ્'}

dental_consonants = {'t':'ત્',
                     'th':'થ્',
                     'd':'દ્',
                     'dh':'ધ્', #Similar to 'the'
                     'n':'ન્'}

labial_consonants = {'p':'પ્',
                     'ph':'ફ્', #As in 'phone'
                     'f':'ફ્',  #As in 'fly'
                     'b':'બ્',
                     'bh':'ભ્',
                     'm':'મ્'}

sonorant_consonants = {'y':'ય્',
                       'r':'ર્',
                       'l':'લ્',
                       'v':'વ્',
                       'w':'વ્'}

sibilant_consonants = {'sh':'શ્',
                       'Sh':'ષ્',
                       's':'સ્'}

guttural_consonants = {'h':'હ્'}

additional_consonants = {'L':'ળ્',
                         'ksh':'ક્શ્',
                         'gn':'ગ્ન્',
                         'ksh':'ક્ષ્'}

consonants = {'k':'ક',
         'c':'ક',
         'kh':'ખ',
         'g':'ગ',
         'gh':'ઘ',
         'ch':'ચ',
         'chh':'છ',
         'j':'જ',
         'z':'ઝ',
         'jh':'ઝ',
         'T':'ટ',
         'Th':'ઠ',
         'D':'ડ',
         'Dh':'ઢ',
         't':'ત',
         'th':'થ',
         'd':'દ',
         'dh':'ધ',
         'n':'ન',
         'p':'પ',
         'ph':'ફ',
         'f':'ફ',
         'b':'બ',
         'bh':'ભ',
         'm':'મ',
         'y':'ય',
         'r':'ર',
         'l':'લ',
         'v':'વ',
         'w':'વ',
         'sh':'શ',
         'Sh':'ષ',
         's':'સ',
         'h':'હ',
         'L':'ળ',
         'ksh':'ક્શ',
         'gn':'ગ્ન',
         'ksh':'ક્ષ​',
         ' ':' '}

#consonants = dict(chain.from_iterable(d.items() for d in (velar_consonants,palatal_consonants,retroflex_consonants,
#                                                          dental_consonants,labial_consonants,sonorant_consonants,
#                                                          sibilant_consonants,guttural_consonants,additional_consonants,full)))

alphabet = dict(chain.from_iterable(d.items() for d in (vowels,consonants,signs)))

letters={'ka':'ક',
         'ca':'ક',
         'kha':'ખ',
         'ga':'ગ',
         'gha':'ઘ',
         'cha':'ચ',
         'chha':'છ',
         'ja':'જ',
         'za':'ઝ',
         'jha':'ઝ',
         'Ta':'ટ',
         'Tha':'ઠ',
         'Da':'ડ',
         'Dha':'ઢ',
         'ta':'ત',
         'tha':'થ',
         'da':'દ',
         'dha':'ધ',
         'na':'ન',
         'pa':'પ',
         'pha':'ફ',
         'fa':'ફ',
         'ba':'બ',
         'bha':'ભ',
         'ma':'મ',
         'ya':'ય',
         'ra':'ર',
         'la':'લ',
         'va':'વ',
         'wa':'વ',
         'sha':'શ',
         'Sha':'ષ',
         'sa':'સ',
         'ha':'હ',
         'La':'ળ',
         'ksha':'ક્શ',
         'gna':'ગ્ન',
         'ksha':'ક્ષ​',
         'a':'અ',
         'aa':'આ',
         'y':'ઇ',
         'i':'ઇ',
         'ee':'ઈ',
         'u':'ઉ',
         'oo':'ઊ',
         'ru':'ઋ',
         'e':'એ',
         'ai':'ઐ',
         'o':'ઓ',
         'au':'ઔ',
         'am':'અં',  
         'ah':'અઃ',
         'an':'અં'}