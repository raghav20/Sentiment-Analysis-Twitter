import csv
import re
import Stemmer
#Stemmer using nltk
from nltk import PorterStemmer
#select column from CSV
def col_selector(table, column_key):
    return [row[column_key] for row in table]

//Createfile
def create_file(rest):
    file = open("Data/out.txt", "w")
    for item in rest:
        file.write("%s\n" % item)


with open("Data/Tweet.csv","r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    table = [row for row in reader]
    foo_col = col_selector(table, "User Name")
    bar_col = col_selector(table, "Tweet")



# Tag Generation For Tweet

lines = [line.strip() for line in open('Data/Stop/stop.txt')]


file = open("Data/b.txt", "w")
for item in foo_col:
    file.write("%s\n" % item)
for item in new_col:
    file.write("%s\n" % item)
file.close()


# Remove Stop Words from Tweets
total =[]
summ = []
rest = []
linef = [line.strip() for line in open('Data/Stop/stop.txt')]
linest = [line.strip() for line in open('Data/Stop/stop2.txt')]
bad_characters = ["/","{","}","\\", ":", "(", ")", "<", ">", "|", "?", "*", ".", "#","&","'","-","$",",","~","[","]",";","@","`","_"]

# Remove Special Charectors
def check_word(word):
    word = word.lower()
    if len(word) > 0:
                if word[-1:] == ",":
                    word = word[:-1]
    for letter in bad_characters:
        word = word.replace(letter,"")
    word = ''.join([i for i in word if not i.isdigit()])
    word = word.replace('\"','')

    if (len(word)>2 and len(word)<10):
        if word not in linef:
            if word not in linest:
                rest.append(word)

# get final list with tags.
with open ("Data/train1.txt") as f:
  lines = f.readlines()
  for line in lines:
      words = line.split()
      for word in words:
          total.append(word)



with open ("Data/train2.txt") as f:
  lines = f.readlines()
  for line in lines:
      words = line.split()
      for word in words:
          total.append(word)


for word in total:
    check_word(word)
    create_file(rest)
    print(len(rest))

# Write tags into file.
ifile = open("Data/out.txt","r")
linelist = ifile.readlines()
linelist.sort()
ifile.close()
ofile = open("Data/out.txt","w")
linelist = "".join(linelist)
ofile.write(linelist)
ofile.close()


lines_seen = set() # holds lines already seen
outfile = open("Data/final.txt", "w")
for line in open("Data/out.txt", "r"):
    str= line.rstrip("\n")
    stem = PorterStemmer().stem_word(str)
    if stem not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(stem)
outfile.close()




