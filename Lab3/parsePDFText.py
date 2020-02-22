import os, glob

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')

from tika import parser

words = []
path = '/Users/diaoqinyu/Desktop/EE460J/Lab3/pdfs'
#write a for-loop to open many files
print('starting')
num_files = 0;
for filename in glob.glob(os.path.join(path, '*.pdf')):
    num_files += 1
    print('reading pdf number ' + str(num_files))

    data_pdf = parser.from_file(filename)
    text = data_pdf["content"]
    #The word_tokenize() function will break our text phrases into #individual words
    tokens = word_tokenize(text)
    #list which contains punctuation we wish to clean
    punctuations = ['(',')',';',':','[',']',',','.','?','=']
    #We create a list comprehension which only returns a list of words #that are and NOT IN punctuations.
    _words = [word for word in tokens if not word in punctuations]
    words = words + _words
    print('total number of words: ' + str(len(words)))
    #print(words)

with open('listOfPDFWords.txt', 'w') as filehandle:
    for listitem in words:
        filehandle.write('%s\n' % listitem)