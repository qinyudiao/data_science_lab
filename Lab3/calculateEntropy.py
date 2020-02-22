from scipy.stats import entropy
from random import random

def sort_by_frequency(alist): 
    dict = {} 
    count, itm = 0, '' 
    for item in reversed(alist): 
        dict[item] = dict.get(item, 0) + 1
    list = sorted(dict.items(), key=lambda x: x[1], reverse=True) 
    return list

words = []

# open file and read the content in a list
with open('listOfPDFWords.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentWord = line[:-1]

        # add item to the list
        words.append(currentWord)

num_words = len(words)
print(num_words)
reverse_words = sort_by_frequency(words)
list_of_frequency = []
list_word_freq_pair = []

total_probrability = 0
for word_freq_pair in reverse_words:
    list_of_frequency.append(word_freq_pair[1]/num_words)
    total_probrability += word_freq_pair[1]/num_words
    list_word_freq_pair.append([word_freq_pair[0], total_probrability])

print("entropy: " + str(entropy(list_of_frequency, base=num_words)))

paragraph = ""
for i in range(0, 100):
    num_rand = random()
    index = 0
    while (num_rand>list_word_freq_pair[index][1]):
        index += 1
    paragraph += list_word_freq_pair[index][0]
    paragraph += " "

print(paragraph)