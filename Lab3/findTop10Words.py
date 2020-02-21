import os, glob

import PyPDF2 
import textract
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')

words = []
path = '/Users/diaoqinyu/Desktop/EE460J/Lab3/pdfs'
#write a for-loop to open many files
print('starting')
num_files = 0;
# for filename in glob.glob(os.path.join(path, '*.pdf')):
for filename in glob.glob(os.path.join('*.pdf')):
    num_files += 1
    print('reading pdf number ' + str(num_files), end = ', ')
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #get the page number
    num_pages = pdfReader.numPages
    print('number of pages: ' + str(num_pages), end = ', ')
    count = 0
    text = ""
    #The while loop will read each page
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        text += pageObj.extractText()
    if text != "":
        text = text
    #else:
    #    text = textract.process(filename, method='tesseract', language='eng')
    print(text)
    #The word_tokenize() function will break our text phrases into #individual words
    tokens = word_tokenize(text)
    #list which contains punctuation we wish to clean
    punctuations = ['(',')',';',':','[',']',',','.','?','1','2','3']
    #We create a list comprehension which only returns a list of words #that are and NOT IN punctuations.
    _words = [word for word in tokens if not word in punctuations]
    words = words + _words
    print('total number of words: ' + str(len(words)))
    #print(words)

def most_frequent(List): 
    dict = {} 
    count, itm = 0, '' 
    for item in reversed(List): 
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count : 
            count, itm = dict[item], item 
    return(itm)

print(most_frequent(words))