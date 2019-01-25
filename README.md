# word-embedding-models
Creating Word Embedding Models for Turkish.

## Prerequisites
* Gensim 3.6.0 
* [Fasttext](https://github.com/facebookresearch/fastText)

## Datasets
* **SynAnalogyTr.txt:** Türkçe için Syntactic Analogy veri kümesi. Toplam 206 adet soru içermektedir. Taken from: Üstün, Ahmet & Kurfalı, Murathan & Can, Burcu. (2018). Characters or Morphemes: How to Represent Words?
* **Turkish-analogy-semantic.txt:** Benim hazırladığım Türkçe için semantic analogy veri kümesi. Toplam 7 farklı kategoride 7742 adet soru içermektedir. Kategori detayları aşağıdaki tablodadır.

| Section Name              | Number Of Questions | 
| --------------------------|:-------------------:| 
| Capital common countries  |   506               | 
| Capital world             |   4446              | 
| City-Department           |   1344              | 
| Family                    |    90               | 
| Currency                  |   156               | 
| Synonyms                  |    600              | 
| Antonyms                  |   600               | 
| Total                     |   7742              | 

* **Anlamver_relatdness.txt:** Türkçe için similarity veri seti. Toplam 500 adet kelime çifti puanlanmıştır. Bu dosyadaki puanlamalar kelimeler arasındaki ilişikiye göre verilmiştir.
* **Anlamver_similarity.txt:** Türkçe için similarity veri seti. Toplam 500 adet kelime çifti puanlanmıştır. Bu dosyadaki puanlamalar kelimeler arasındaki benzerliğe göre verilmiştir.
* **Anlamver-final.csv:** Orijinal veri kümesi. Ölçümleme yapabilmek için bu excelden yukarıdaki iki adet dosyayı oluşturdum. Taken from: Ercan, Gokhan & Yildiz, Olcay. (2018). AnlamVer: Semantic Model Evaluation Dataset for Turkish-Word Similarity and Relatedness.

## Models
- **all-combined-plus-trwiki-lower-higher100-w2v-cbow.bin:** all_combined_plus_trwiki_lowercase_100.txt corpusu üzerinde word2vec ile size=300, window=5, min_count=5, sg=0, negative=5 parametreleri ile eğitildi.
- **all-combined-plus-trwiki-lower-higher100-skigram-3-0ng-5neg.bin:** all_combined_plus_trwiki_lowercase_100.txt corpusu üzerinde fasttext ile model=’skipgram’, dim=300, minCount=5, ws=5, neg=5, minn=3 ve maxn=0 parametreleri ile eğitildi.

## Corpus
* **all_combined_plus_trwiki_lowercase_100.txt:**
* **wiki-tr-lastest.txt:** trwiki-20181101-pages-articles.xml.bz2 (https://dumps.wikimedia.org/trwiki/20181101/) dosyasının gensim kütüphanesindeki WikiCorpus fonksiyonu ile extract edilmiş halidir.
