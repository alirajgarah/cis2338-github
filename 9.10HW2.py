#Ali Rajgarah 1586471

import csv
freq={}
filename=input()
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    line=next(csvreader)
    for word in line:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
for i in freq:
    print(i, freq[i])