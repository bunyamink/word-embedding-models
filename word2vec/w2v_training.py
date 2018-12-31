'''
Bunyamin Kurt - ITU Graduation Project 2018
This file for training to corpus with word2vec.
In corpus file there must be one sentence in one line.
'''

from gensim.models import word2vec
import logging
from gensim.models.word2vec import LineSentence
import multiprocessing
from gensim.models import FastText

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Train Corpus
model = word2vec.Word2Vec(LineSentence('../corpuses/wiki-tr-lastest.txt'), size=300, window=5, min_count=5, sg=1, negative=5, workers=multiprocessing.cpu_count())
# Save Model 
model.wv.save_word2vec_format("../models/wiki-models/wiki-tr-lastest-skipgram-w2v.bin", binary=True)

# vec format file to bin file for facebook pre trained model
#embedding_dict = gensim.models.KeyedVectors.load_word2vec_format(dictFileName, binary=False)
#embedding_dict.save_word2vec_format(dictFileName+".bin", binary=True)
#embedding_dict = gensim.models.KeyedVectors.load_word2vec_format(dictFileName+".bin", binary=True)
