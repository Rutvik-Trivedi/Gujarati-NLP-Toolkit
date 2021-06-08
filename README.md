
# Gujarati-NLP-Toolkit


## Added Features:

### 1) POS Tagger:

#### a) Implementation:
```python
import posTagger as pt
tagger = pt.posTagger(corpus='prose')	# corpus='poetry' if you are tagging a sentence of a poem
tagger.eval()	# Set the tagger in evaluation/inference mode
sentence = 'તારુ નામ શુ છે?'  # What is your name?
print(tagger.pos_tag(sentence))   # [('તારુ', 'PR_PRP'), ('નામ', 'N_NN'), ('શુ', 'N_NN'), ('છે', 'V_VAUX'), ('?', 'RD_PUNC')]
```

#### b) Training your own posTagger:
```python
import posTagger as pt
tagger = pt.posTagger('model_name')   # Give any name for your model
train_data = tagger.structure_data('path/to/corpus/file')
```

Your corpus must be in txt(tab delimited) or tsv format (as having csv might conflict because Gujarati has the comma \[ , \] as a punctuation) and must contain a column 'Value' having the data in the form:
```
Row1:    'word1\tag1 word2\tag2 word3\tag3 ....... wordn\tagn'
Row2:    'word1\tag1 word2\tag2 word3\tag3 ....... wordn\tagn'
```

Else You may create your own train_X, train_y of the form:
```
train_X:  [[feature_dict of word1, feature_dict of word2, ........ , feature_dict of wordn],     //Sentence 1
	      [feature_dict of word1, feature_dict of word2, ........ , feature_dict of wordn]]	   // Sentence n
train_y:  [[tags of sentence 1], [tags of sentence 2], ........, [tags of sentence n]]
```
&nbsp;

>Moreover, you may also train data in languages other than Gujarati for creating posTagger in your own language.

&nbsp;

Enter the Following block of code after this:

```python
tagger.train(train_data, tagger._model_file)
```

#### c)  Loading your trained posTag Model:
```python
import posTagger as pt
tagger = pt.posTagger('model_name')
tagger.eval()
## Carry out your processes
```


&nbsp;
&nbsp;
### 2) Tokenizers:

#### a)  Word Tokenizer:

```python
from tokenizer import WordTokenizer
sentence = 'તારુ નામ શુ છે?'  # What is your name?
tokens = WordTokenizer(sentence, keep_punctuations=True, keep_stopwords=True)   # Set False to remove Punctuations and Stopwords respectively
print(tokens)  # ['તારુ', 'નામ', 'શુ', 'છે', '?']
```

#### b)  Sentence Tokenizer:

```python
from tokenizer import SentenceTokenizer
sentence = 'તારુ નામ શુ છે? તુ શુ કરે છો?'  # What is your name? What are you doing?
tokens = SentenceTokenizer(sentence)
print(tokens)  # ['તારુ નામ શુ છે?', 'તુ શુ કરે છો?']
```
&nbsp;
&nbsp;
### 3) Transliterator:
This feature is helpful for people not acquainted with Gujarati. This function takes input of a Gujarati Word or Letter and gives out the Pronounciation of the respective input in English.

#### a) Letter Transliteration:
```python
from transliterator import Transliterator
transliterator = transliterator()
transliteration = transliterator.letter_transliterate_gujarati_to_english('ત')  # Letter 'ta'
print(transliteration)   # ta
```

#### b) Word/Sentence Translation:
```python
from transliterator import Transliterator
transliterator = transliterator()
transliteration = transliterator.transliterate('તારુ')  # Meaning 'your' or 'yours'
print(transliteration)   # taaru
transliteration = transliterator.transliterate('મારુ નામ રુત્વિક છે')	# meaning 'My name is Rutvik'
print(transliteration)   # maaru naam rutvik chhe
```
&nbsp;
&nbsp;
### 4) Stemmer:
The implementation of the Stemmer is completely rule based. So, it will not be able to give accurate stems and meaningful words. The stemmer is able to give stemmed words by stripping both prefixes and suffixes. An example covering both the strips is given below. The implementation of the stemmer can be done as follows:

#### a) Stem a text:
```python
from stemmer import Stemmer
stemmer = Stemmer()
example_text = 'હું દોડ​વા જઉં છું. દોડ​વા માટે તમારે સાથે આવ​વું પ‌ડશે. ચાલશે ને? અન્યાય ના કરતા.'
# Meaning: 'I am going for a run. You will have to come with me. Is it ok? Don't be unfair.'
# This will exhibit both prefix (in 'અન્યાય') and suffix (in 'દોડ​વા' and other words) stripping.
stemmed_text = stemmer.stem(example_text)
print(stemmed_text)
# Output is a list of stemmed sentences: ['હુ દોડ જઉં છું.', 'દોડ માટે તમાર સાથ ચાલ પડશ.', 'ચાલશ ને', 'ન્યાય ના કર.']
```

#### b) Add and Remove Suffixes:
```python
from stemmer import Stemmer
stemmer = Stemmer()
stemmer.add_suffix('suffix_in_gujarati') # Will add the entered suffix to the stripping list. Will strip the suffix after this
stemmer.stem('your_sentence') # This sentence will be stripped of your added suffix also.
stemmer.add_prefix('prefix_in_gujarati') # Similar to add_suffix(). But it will work for prefix.
stemmer.delete_suffix('suffix_to_delete') # Stemmer won't consider stripping the suffix anymore for the session.
stemmer.delete_prefix('prefix_to_delete') # Similar to delete_suffix() but for prefix.
```

&nbsp;
&nbsp;

# TODO:
- Improve the POS Tagger performance
- Create a morphological tokenizer
- Create a Sentiment Analyser
