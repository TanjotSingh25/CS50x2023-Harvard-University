def counter( s, o):
    count = 0
    s = str(s)
    o = str(o)
    for i in range(len(s)):
        if s.find(o) != -1:
            count += 1
            s = s[ s.find(o) + len(o) : ]
            continue
        elif s.find(o) == -1:
            break
    return (count)


import csv
from sys import exit
from sys import argv

if len(argv) != 3:
    print("Usage error: dna.py database/<name of data base>.csv sequence/<name of file>.txt")
    quit()

with open(argv[2], "r") as personDNA :
    readDNA = csv.reader(personDNA)
    for row in readDNA:
        dna = row
        break
dna = str(dna)

lists = ["AGATC","TTTTTTCT","AATG","TCTAG","GATA","TATC","GAAA","TCTG"]
storage = []

for i in range(8):
    storage.append(counter(dna , lists[i]))


print(storage)
with open(argv[1], "r") as database:
    read_database = csv.reader(database)
    next(read_database)
    for row in read_database:
        if row[1] == storage[1] and row[2] == storage[2] and row[3] == storage[3] and row[4] == storage[4] and row[5] == storage[5] and row[6] == storage[6] and row[7] == storage[7] and row[8] == storage[8]:
            print(f"This DNA is of :{row[0]}")