'''
Bunyamin Kurt - ITU 2018
'''
import codecs

def main():
    dictionary = getDict()
    file = codecs.open("analogy-data-sets/google_currency_en.txt", "r", "utf-8")
    result_file = codecs.open('analogy-data-sets/google_currency_tr.txt', 'w', 'utf-8')
    for line in file:
        if(line[0] == ":"): continue
        words = line.split(" ")
        result_file.write(dictionary[words[0].lower()] + " " + dictionary[words[1].lower()] + " " + dictionary[words[2].lower()] + " " + dictionary[words[3].strip("\n").strip("\r").lower()] + "\n")
    result_file.close()


def getDict():
    file = codecs.open("a.txt", "r", "utf-8")
    dict = {}
    for line in file:
        words = line.split("\t")
        dict[words[0]] = words[1].strip("\n").strip("\r")
    return dict



if __name__ == '__main__':
    main()
