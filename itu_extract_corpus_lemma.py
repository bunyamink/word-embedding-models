''' 
Bunyamin Kurt - ITU 2018
This file extract the lemmazation corpus from morphological analyzer corpus.
'''
import io

def main():
    combine()

def combine():
    files = [
    'corpuses/wiki-corpus/wiki-tr-lastest.txt',
    'corpuses/our-big-corpus/alltext.autoTokenized.autoSentenceSplit.ituMorphTagged_lemma.txt',
    'corpuses/our-big-corpus/gencor.autoSentenceSplit.ituMorphTagged.v2_lemma.txt',
    'corpuses/our-big-corpus/milliyet-clean-utf.sentences.ituMorphTagged_lemma.txt',
    'corpuses/our-big-corpus/newscor.autoSentenceSplit.ituMorphTagged.v2_lemma.txt',
    'corpuses/our-big-corpus/sentences6-UTF8.ituMorphTagged_lemma.txt'
    ]
    #files = ["a.txt","b.txt"]
    outFile = open('corpuses/our-big-corpus/all_combined_lemma_plus_trwiki.txt', "w", encoding='utf-8')
    for file in files:
        f = open(file, "r", encoding='utf-8')
        for line in f:
            outFile.write(line)

def extract_corpus_lemma():

    f = open('C:/Users/Bunyamin/Desktop/Okul Dersleri/Graduation Project/Data Sets/corpuses/Türkçe ITU Tugba Hoca/sentences6-UTF8.ituMorphTagged.txt', 'r', encoding='utf-8')
    outFile = open('corpuses/our-big-corpus/sentences6-UTF8.ituMorphTagged_lemma.txt', "w", encoding='utf-8')

    punc = ['.', ',', '!', '?', ';', ':', '-', "'", '"', '(', ')']
    for line in f:
        words = line.split(" ")

        if(words[0] == '\n' or len(words) <= 1):
            outFile.write("\n")
            continue

        lemma_words = words[1].split("+")

        if(lemma_words[0] in punc):
            continue
        outFile.write(lemma_words[0])
        outFile.write(" ")

if __name__ == '__main__':
    main()
