import csv
import re
import Stemmer

def column_selector(table, column_key):
    return [row[column_key] for row in table]


# File containing tweet information . 
with open("Data/Captain America.csv","r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    table = [row for row in reader]
    bar1_col = column_selector(table, "Tweet")

with open("Data/Captain America(2).csv","r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    table = [row for row in reader]
    bar2_col = column_selector(table, "Tweet")

with open("Data/Captain America(3).csv","r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    table = [row for row in reader]
    bar3_col = column_selector(table, "Tweet")

with open("Data/Captain America(4).csv","r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    table = [row for row in reader]
    bar4_col = column_selector(table, "Tweet")


file = open("Data/ca.txt", "w")
for item in bar1_col:
    file.write("%s\n" % item)
for item1 in bar2_col:
    file.write("%s\n" % item1)
for item2 in bar3_col:
    file.write("%s\n" % item2)
for item3 in bar4_col:
    file.write("%s\n" % item3)



