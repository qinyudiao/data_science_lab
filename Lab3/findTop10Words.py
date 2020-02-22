
def most_frequent(alist): 
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

reverse_words = most_frequent(words)
for i in range(0,10):
    print(reverse_words[i])