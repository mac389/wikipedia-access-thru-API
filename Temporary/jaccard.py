# -*- coding: utf-8 -*-
import nltk
from nltk.collocations import *
def bigramFinder(FileA):
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    with open(FileA,'rb') as infile:
        finder = BigramCollocationFinder.from_words(nltk.word_tokenize(infile.read()))  
    bigrams = finder.nbest(bigram_measures.pmi, 20)
    print bigrams

bigramFinder("sanitizted")
bigramFinder("sanitized2")
bigramFinder("sanitized3")

def jaccard(file1, file2):
    set1 = set(open(file1,'rb').read().splitlines())    
    set2 = set(open(file2,'rb').read().splitlines())
    return float(len(set1 & set2))/len(set1 | set2)
    
print jaccard('sanitizted', 'sanitized2')
print jaccard('sanitizted', 'sanitized3')
print jaccard('sanitized2', 'sanitized3')

