'''
Bunyamin Kurt - ITU Graduation Project 2018
This file for evaluate to models.
Evaluate for analogy and similarity task.
'''

from gensim.models import word2vec
from gensim.models import FastText
from gensim import matutils
import gensim
import io
import logging
import codecs

def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    #model = gensim.models.Word2Vec.load('./models/nltk/tr.bin')
    #model = gensim.models.KeyedVectors.load_word2vec_format('../models/itu-models/all-combined-plus-trwiki-w2v.bin', binary=True)
    #model = gensim.models.KeyedVectors.load_word2vec_format('../models/70_nlpl/model.txt', binary=False, unicode_errors='replace')
    model = FastText.load_fasttext_format('../models/itu-models/new/all-combined-plus-trwiki-lower-higher100-cbow-3-0ng-5neg.bin')
    #model = FastText.load_fasttext_format('../models/facebook-fasttext/cc.tr.300_facebook_fasttext_new.bin')
    #model = FastText.load('./models/trwiki_lastest_model_fasttext.bin')

   
    analogy_accuracy("../analogy-data-sets/Turkish/turkish_analogy.txt", model)
    analogy_accuracy("../analogy-data-sets/Turkish/SynAnalogyTr.txt", model)
    
    similarity("../similarity-data-sets/turkish/anlamver_similarity.txt",model)
    similarity("../similarity-data-sets/turkish/anlamver_relatdness.txt",model)

def analogy_accuracy(filename,model):

    accuracy = model.accuracy(filename, restrict_vocab=200000)

    # After gensim version 3.6 use these function.
    #accuracy = model.evaluate_word_analogies(filename, restrict_vocab=500000)

    sum_corr = len(accuracy[-1]['correct'])
    sum_incorr = len(accuracy[-1]['incorrect'])
    total = sum_corr + sum_incorr
    percent = lambda a: a / total * 100

    print('Total sentences: {}, Correct: {:.2f}%, Incorrect: {:.2f}%'.format(total, percent(sum_corr), percent(sum_incorr)))

def similarity(filename,model):
    result = model.evaluate_word_pairs(filename)


if __name__ == '__main__':
    main()

