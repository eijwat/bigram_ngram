# August 2022
# python3 gram_main.py
# python3 gram_main.py > log.txt
#Unigrams(ugs), Bigrams(bgs), Trigram(tgs), Ngrams(ngs)


import nltk
from nltk.util import ngrams


#========== n of ngram ========== option = ngram
n = 5
#========== n of ngram ==========

#open text file
f = open('heidi/heidi.txt','r')
#f = open('wikitext-103/wiki.train.tokens','r')

#create token
universe = ""
for val in f:
    universe += val
tokens = universe.split()

#close text file
f.close()

#Create ngrams
ugs = tokens
bgs = nltk.bigrams(tokens)
tgs = nltk.trigrams(tokens)

#option = ngram
"""
ngs = ngrams(tokens, n)

#compute frequency distribution for ngrams in the text
# print and save frequency
fdist = nltk.FreqDist(ngs)
f = open('freq_ngs.txt', 'w')
for k,v in fdist.items():
    print (k,v)
    f.write(str(k)+str(v)+'\n')
f.close()
"""

#compute frequency distribution for ngrams in the text
#print and save frequency
fdist = nltk.FreqDist(tgs)
f = open('freq_tgs.txt', 'w')
for k,v in fdist.items():
    print (k,v)
    f.write(str(k)+str(v)+'\n')
f.close()

#compute frequency distribution for ngrams in the text
#print and save frequency
fdist = nltk.FreqDist(bgs)
f = open('freq_bgs.txt', 'w')
for k,v in fdist.items():
    print (k,v)
    f.write(str(k)+str(v)+'\n')
f.close()


#compute frequency distribution for ngrams in the text
#print and save frequency
fdist = nltk.FreqDist(ugs)
f = open('freq_ugs.txt', 'w')
for k,v in fdist.items():
    print (k,v)
    f.write(r"('" + str(k) + r"')" + str(v)+'\n')
f.close()
