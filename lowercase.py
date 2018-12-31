'''
Bunyamin Kurt - ITU Graduation Project 2018
This file for converting to corpus to lowercase and delete sentence less than 100 character.
'''
import unicodedata

file = open('../corpuses/our-big-corpus/all_combined_lemma_lower_100.txt', 'r', encoding='utf-8')
outputfile = open('../corpuses/our-big-corpus/all_combined_lemma_plus_trwiki_lower_100.txt', 'w', encoding='utf-8')

def strip_accents(string, accents=('COMBINING ACUTE ACCENT', 'COMBINING GRAVE ACCENT', 'COMBINING TILDE', 'COMBINING CARON', 'COMBINING DOT ABOVE')):
    accents = set(map(unicodedata.lookup, accents))
    chars = [c for c in unicodedata.normalize('NFD', string) if c not in accents]
    return unicodedata.normalize('NFC', ''.join(chars))


for line in file:
	if len(line) <= 100:
		continue
	words = line.split(" ")
	j = 0
	for word in words:
		outputfile.write(strip_accents(word.lower()))
		j += 1
		if j >= len(words):
			break
		outputfile.write(" ")
