import csv
import re
import Stemmer

from nltk import PorterStemmer

def col_selector(table, column_key):
    return [row["Word"]+","+row["V.Mean.Sum"]+","+row["V.SD.Sum"]+","+row["A.Mean.Sum"]+","+row["A.SD.Sum"]+","+row["D.Mean.Sum"]+","+row["D.SD.Sum"] for row in table]
from nltk import PorterStemmer
def colu_selector(table, column_key):
    return [row["Word"]+","+row["ValMn"]+","+row["ValSD"]+","+row["AroMn"]+","+row["AroSD"]+row["DomMn"]+","+row["DomSD"] for row in table]

with open("Data/Ratings_Warriner_et_al.csv","r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    table = [row for row in reader]
    bar1_col = col_selector(table, "V.Mean.Sum")
    #bar2_col = col_selector(table, "V.SD.Sum")
    #bar3_col = col_selector(table, "A.Mean.Sum")
    #bar4_col = col_selector(table, "A.SD.Sum")
    #bar5_col = col_selector(table, "D.Mean.Sum")
    #bar6_col = col_selector(table, "D.SD.Sum")

with open("Data/Ratings_Warriner_et_al.csv","r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    table = [row for row in reader]
    bar1_col = col_selector(table, "V.Mean.Sum")

with open("Data/ANEW2010All.csv","r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    table = [row for row in reader]
    bar2_col = colu_selector(table, "Word")

file = open("Data/test.csv", "w")
file.write("Word,V.Mean.Sum,V.SD.Sum,A.Mean.Sum,A.SD.Sum,D.Mean.Sum,D.SD.Sum\n")
for item in bar1_col:
    file.write("%s\n" % item)

for item in bar2_col:
    file.write("%s\n" % item)


#reader = csv.DictReader(open('Data/test.csv', 'r'))
#result = sorted(reader, key=lambda d: float(d['Word']))

#writer = csv.DictWriter(open('Data/new.csv', 'w'), reader.fieldnames)
#writer.writeheader()
#writer.writerows(result)





