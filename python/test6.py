import csv

with open("aaa.tsv", "r") as f:
    for cols in csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
        print(cols)