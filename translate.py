'''
Bunyamin Kurt - ITU 2018
Google translate api for translating english analogy task to Turkish
'''
from googletrans import Translator
import codecs

translator = Translator()

translated_words = []

i = 0
with open('google_for_turkish.txt') as f:
    content = f.readline()
    while content:
        #if(i == 50): break
        if(content[:1] == ":"):
            content = f.readline()
            continue
        words = content.split(" ")
        try:
            translated_word1 = translator.translate(words[0].strip("\n"), src="en", dest="tr")
            translated_word2 = translator.translate(words[1].strip("\n"), src="en", dest="tr")
            translated_word3 = translator.translate(words[2].strip("\n"), src="en", dest="tr")
            translated_word4 = translator.translate(words[3].strip("\n"), src="en", dest="tr")
        except:
            content = f.readline()
            print("Raise error")
            continue
        if(translated_word1.text and translated_word2.text and translated_word3.text and translated_word4.text):
            translated_words.append([])
            translated_words[i].append(translated_word1.text.lower())
            translated_words[i].append(translated_word2.text.lower())
            translated_words[i].append(translated_word3.text.lower())
            translated_words[i].append(translated_word4.text.lower())
            i += 1
        content = f.readline()

#print(translated_words)
result_file = codecs.open('google_turkce.txt', 'w', 'utf-8')
for t in translated_words:
    result_file.write(t[0] + " " + t[1] + " " + t[2] + " " + t[3] + "\n")
result_file.close()
