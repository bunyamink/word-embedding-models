'''
Bunyamin Kurt - ITU 2018
This for prepare the es anlamli analogy data set from 25 words.
'''

import codecs

def a():
    file = codecs.open("zit_anlamlilar_result.txt", "r", "utf-8")
    x = []
    y = []
    for line in file:
        line = line.strip("\n").strip("\r")
        words = line.split(" - ")
        for word in words:
            if word in x:
                y.append(word)
                continue
            else:
                x.append(word)
    print(y)

def b():
    file = codecs.open("zit_anlamlilar.txt", "r", "utf-8")
    a = []
    for line in file:
        line = line.strip("\n").strip("\r")
        words = line.split("-")
        a.append(words)

def prepareAnalogy():
    file = codecs.open("./similarity-data-sets/turkish/para_birimi.txt", "r", "utf-8")
    result_file = codecs.open('./similarity-data-sets/turkish/para_birimi_analogy.txt', 'w', 'utf-8')
    x = []
    i = 0
    for line in file:
        line = line.strip("\n").strip("\r")
        words = line.split(" ")
        x.append([])
        x[i].append(words[0])
        x[i].append(words[1])
        i += 1

    for line in x:
        for l in x:
            if line[0] != l[0]:
                result_file.write(line[0] + " " + line[1] + " ")
                result_file.write(l[0] + " " + l[1] + "\n")
        result_file.write("\n")

def main():
    prepareAnalogy()
    '''file = codecs.open("zit_anlamlilar.txt", "r", "utf-8")
    dict = {}
    for line in file:
        line = line.strip("\n").strip("\r")
        words = line.split("-")
        for index, word in enumerate(words):
            if index == 0:
                dict[words[0]] = []
                continue
            dict[words[0]].append(word)

    new_dict = {}
    for key, values in dict.items():
        x = []
        exist_key = False
        k = False
        for value in values:
            if value in new_dict:
                exist_key = True
                k = value
                continue
            else:
                x.append(value)
        if x and not exist_key:
            new_dict[key] = x
        if x and exist_key and k:
            new_dict[k] = new_dict[k] + x

    result_file = codecs.open('zit_anlamlilar_result.txt', 'w', 'utf-8')
    for key, values in new_dict.items():
        result_file.write(key)
        for value in values:
            result_file.write(" - " + value)
        result_file.write("\n")'''

if __name__ == '__main__':
    main()
