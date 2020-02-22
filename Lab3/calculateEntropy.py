from scipy.stats import entropy
import random


def sort_by_frequency(alist): 
    dict = {} 
    count, itm = 0, '' 
    for item in reversed(alist): 
        dict[item] = dict.get(item, 0) + 1
    list = sorted(dict.items(), key=lambda x: x[1], reverse=True) 
    return list


words = []

# open file and read the content in a list
with open('listOfPDFWords.txt', 'r', encoding='utf8') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentWord = line[:-1]

        # add item to the list
        words.append(currentWord)

num_words = len(words)
reverse_words = sort_by_frequency(words)
list_of_frequency = []
list_word_freq_pair = []

total_probrability = 0
for word_freq_pair in reverse_words:
    list_of_frequency.append(word_freq_pair[1]/num_words)
    total_probrability += word_freq_pair[1]/num_words
    list_word_freq_pair.append([word_freq_pair[0], total_probrability])

print("Entropy: " + str(entropy(list_of_frequency, base=num_words)))
print()

num_words_para = 200
paragraph = ""
len_counter = 0

for word in range(num_words_para):
    pick = random.randint(0, num_words)
    i = 0
    done = False
    total = 0
    while i < num_words and not done:
        pair = reverse_words[i]
        total += pair[1]
        if total > pick:
            paragraph += pair[0]
            paragraph += " "
            done = True
            len_counter += len(pair[0])
            if len_counter > 100:
                paragraph += "\n"
                len_counter = 0
        i += 1

print(paragraph)