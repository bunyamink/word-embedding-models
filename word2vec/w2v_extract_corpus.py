'''
Bunyamin Kurt - ITU Graduation Project 2018
This file for extract the corpus from morphological analyzer.
'''

from gensim.models import word2vec
from gensim import matutils
import gensim
import io
import logging

import multiprocessing

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

f = open('alltext.autoTokenized.autoSentenceSplit.ituMorphTagged_extracted.txt', 'r', encoding='utf-8')
outFile = open('all_combined_plus_trwiki.12.11.2018.txt', "w", encoding='utf-8')

punc = ['.', ',', '!', '?', ';', ':', '-', "'", '"', '(', ')']

#documents = []
#documents.append([])
#i = 0
for line in f:
    outFile.write(line)
    words = line.split(" ")
    if(words[0] == '\n' or len(words) <= 1):
        outFile.write("\n")
        #documents.append([])
        #i += 1
        #continue
    if(words[0] in punc):
        continue
    #documents[i].append(words[0])
    outFile.write(words[0])
    outFile.write(" ")

