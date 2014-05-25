# Cosine Similarity between files. Another Way of getting the similarity.

import csv
import re
import Stemmer


#Stemmer using nltk
from nltk import PorterStemmer
#select column from CSV
def col_selector(table, column_key):
    return [row[column_key] for row in table]

with open("Data/Tweet.csv","r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    table = [row for row in reader]
    name_col = col_selector(table, "User Name")
    tweet_col = col_selector(table, "Tweet")


file = open("Data/alltweet.txt", "w")
for item in bar_col:
    file.write("%s\n" % item)
    
    

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform("Data/alltweet.txt")
print(tfidf_matrix.shape)
from sklearn.metrics.pairwise import cosine_similarity
print(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix))
