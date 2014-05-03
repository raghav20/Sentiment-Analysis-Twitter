import csv
import re
import Stemmer
import nltk
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews

def strip_bits(obj):
    for el in obj:
        yield el[1:-1]

def word_feats(words):
    return dict([(word, True) for word in words])

with open('Data/test.csv') as fin:
    tempin = strip_bits(fin)
    csvin = csv.reader(tempin)

            #print(row[0]) # or do whatever



negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]

negcutoff = len(negfeats)*3/4
print(negcutoff)
poscutoff = len(posfeats)*3/4

trainfeats = negfeats[:int(negcutoff)] + posfeats[:int(poscutoff)]
testfeats = negfeats[int(negcutoff):] + posfeats[int(poscutoff):]
print('train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats)))

classifier = NaiveBayesClassifier.train(trainfeats)
print('accuracy:', nltk.classify.util.accuracy(classifier, testfeats))
classifier.show_most_informative_features()


