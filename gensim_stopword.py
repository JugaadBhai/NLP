# pip install gensim
from gensim.parsing.preprocessing import STOPWORDS
from gensim.parsing.preprocessing import remove_stopwords
import gensim
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
text = "Sam likes to play cricket, however he is not too fond of baseball."
filtered_sentence = remove_stopwords(text)
print(filtered_sentence)
all_stopwords = gensim.parsing.preprocessing.STOPWORDS
print(all_stopwords)
all_stopwords_gensim = STOPWORDS.union(set(['likes', 'play']))
text = "Sam likes to play cricket, however he is not too fond of baseball."
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in
                     all_stopwords_gensim]
print(tokens_without_sw)
all_stopwords_gensim = STOPWORDS
sw_list = {"not"}
all_stopwords_gensim = STOPWORDS.difference(sw_list)
text = "Sam likes to play cricket, however he is not too fond of baseball."
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in
                     all_stopwords_gensim]
print(tokens_without_sw)
