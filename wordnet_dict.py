# Wordnet provides synsets which is the collection of synonym words aslo called lemmas

import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

print(wordnet.synsets('computer'))

# Definition and example of the word `computer`
print(wordnet.synset('computer.n.01').definition())

# examples
print('Examples:', wordnet.synset('computer.n.01').examples())

# get antonyms
print('Antonyms:', wordnet.lemma('buy.v.01.buy').antonyms())