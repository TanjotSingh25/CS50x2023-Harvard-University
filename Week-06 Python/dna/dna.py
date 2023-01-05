import sys  # for argv
import csv  # for csv reader


def main():

    # return if argv not up to requirements
    if len(sys.argv) != 3:
        print("Usage: dna.py database.csv sequence.txt")
        return 0

    list = []  # stores the database in list form
    maxi = []  # stores the maximum iterations in list form

    database = open(sys.argv[1])
    reader = csv.reader(database)

    # stores database in list of list forms
    for row in reader:
        list.append(row)

    seq = open(sys.argv[2])
    s = seq.read()  # reads the sequence file and stores it in the form of a string
    l = len(list[0])
    i = j = k = 1
    while i < l:
        pat = list[0][i]
        maxi.append(count(pat, s))
        print('F: ',count(pat, s))
        print('M: ',s.count(pat))
        i += 1

    while j < len(list):
        x = 0
        k = 1
        while k < len(list[j]):
            if list[j][k] == maxi[k - 1]:
                x += 1
                k += 1
            else:
                break
        if x == (len(list[0]) - 1):
            print(list[j][0])
            return
        j += 1

    print("No Match")


# function to return maximum iterations of a perticular pattern in a sequence
def count(pat, seq):
    max = 0
    t = 1
    l = len(seq)
    a = seq.find(pat)
    seq = seq[seq.find(pat) + len(pat):l]
    while True:
        if seq.find(pat) == 0:
            t += 1
            seq = seq[len(pat):l]
        else:
            if t > max:
                max = t
            t = 1
            seq = seq[seq.find(pat) + len(pat):len(seq)]

        if seq == "":
            break

    return str(max)


main()