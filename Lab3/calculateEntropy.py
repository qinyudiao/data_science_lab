from scipy.stats import entropy

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
reverse_words = sort_by_frequency(words)
list_of_frequency = []
for word_freq_pair in reverse_words:
    list_of_frequency.append(word_freq_pair[1]/num_words)

print("entropy: " + str(entropy(list_of_frequency, base=num_words)))
