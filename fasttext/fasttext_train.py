'''
Bunyamin Kurt - ITU Graduation Project 2018
This file for training to corpus with fasttext.
'''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division, absolute_import, print_function

from fastText import train_unsupervised
import os

if __name__ == "__main__":
    model = train_unsupervised(
        input=os.path.join(os.getenv("DATADIR", '..\\corpuses'), 'wiki-tr-lastest.txt'),
        model='cbow',
        dim=300,
        minCount=5,
        ws=5,
        neg=5,
        minn=3,
        maxn=6
    )
    model.save_model("wiki-tr-lastest-fasttext.bin")
    #dataset, corr, oov = compute_similarity('similarity-data-sets/turkish/anlamver_similarity.txt')
    #print("{0:20s}: {1:2.0f}  (OOV: {2:2.0f}%)".format(dataset, corr, 0))
    #compute_analogy("..\\analogy-data-sets\Turkish\turkish_analogy.txt")
