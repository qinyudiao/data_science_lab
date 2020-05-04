# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
# from nltk.tokenize import WordPunctTokenizer
# from nltk.collocations import BigramCollocationFinder
# from nltk.metrics import BigramAssocMeasures
import random as rand
from random import random

import enchant
d = enchant.Dict("en_US")


sentences = []
temps = []
# open file and read the content in a list
with open('listOfPDFWords.txt', 'r') as filehandle:
    count = 0
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentWord = line[:-1]
        # add item to the list
        temps.append(currentWord)

        # sentences.append(temps)
        # if count == 300:
        #     count = 0
        #     sentences.append(temps)
        #     temps = []
        # else:
        #     count += 1
sentences.append(temps)

bigrams = {}
for line in sentences:
    try:
        empty_list = []
        for i in range(0, len(line)):
            if bigrams.get(line[i]) is None:
                bigrams[line[i]] = [1]
        for i in range(0, len(line)-1):
            list_v = bigrams[line[i]]
            list_v[0] = list_v[0]+1
            list_v.append(line[i+1])
            bigrams[line[i]] = list_v
    except:
        continue

total_value = 0
sum = 0
dictlist = []
for key, value in bigrams.items():
    temp = [key,value]
    dictlist.append(temp)
for listitem in dictlist:
    total_value += listitem[1][0]
for listitem in dictlist:
    sum += listitem[1][0] / total_value
    listitem[1][0] = sum

def random_next():
    num_rand = random()
    print(num_rand)
    print(dictlist[0][1][0])
    index = 0
    while (num_rand>dictlist[index][1][0]) and index < len(dictlist):
        index += 1
    return dictlist[index][0]

paragraph = ""
next_word = None
for i in range(0,100,1):
    if next_word is None:
        next_word = random_next()
    paragraph += next_word
    paragraph += " "
    if bigrams.get(next_word) is None:
        next_word = random_next()
    else:
        list_temp = bigrams[next_word][1:]
        next_word = rand.choice(list_temp)

print(paragraph)