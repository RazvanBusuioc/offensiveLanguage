import csv
import os
import random

#80% Train
#20% Test

#MINIMUM SENTENCE LEN = 15 chars
#MAXIMUM SENTENCE LEN = 187 chars

finalSet = []

file = open("dataset.csv", "r")
reader = csv.reader(file)
next(reader)

other = 0
offensive = 0
min = 1000
max = 0
for row in reader:
    if (len(row[2]) > max):
        max = len(row[2])
    if (len(row[2]) < min):
        min = len(row[2])
    if(row[3] == "OTHER"):
        if (other >= 2673): # 2637 = 1.5 * NUMBER_OF_OFF_SENTENCES
            continue
        other += 1
    finalSet.append(row)

file.close()

random.shuffle(finalSet)
datasetLen = len(finalSet)
trainLen = int(0.8 * datasetLen)
testLen = datasetLen - trainLen
print("Train len: " + str(trainLen))
print("Test len: " + str(testLen))

print("Min sentence len is " + str(min))
print("Max sentence len is " + str(max))

file = open("cutDataset.csv", "w")
writer = csv.writer(file)
writer.writerow(["sender","no_reacts","text","label"])
writer.writerows(finalSet)
file.close()


file = open("train.csv", "w")
writer = csv.writer(file)
writer.writerow(["sender","no_reacts","text","label"])
writer.writerows(finalSet[:trainLen])
file.close()

file = open("test.csv", "w")
writer = csv.writer(file)
writer.writerow(["sender","no_reacts","text","label"])
writer.writerows(finalSet[trainLen:])
file.close()

