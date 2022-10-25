import csv
import os
import random


#80% internal_train
#20% internal_validate

set = []

file = open("train.csv", "r")
reader = csv.reader(file)
next(reader)

for row in reader:
    set.append(row)

file.close()

random.shuffle(set)

setLen = len(set)
internalTrainLen = int(0.8 * setLen)
internalValidateLen = setLen - internalTrainLen

print("internal train len: " + str(internalTrainLen))
print("internal validate len: " + str(internalValidateLen))


file = open("train_internal.csv", "w")
writer = csv.writer(file)
writer.writerow(["sender","no_reacts","text","label"])
writer.writerows(set[:internalTrainLen])
file.close()

file = open("validation_internal.csv", "w")
writer = csv.writer(file)
writer.writerow(["sender","no_reacts","text","label"])
writer.writerows(set[internalTrainLen:])
file.close()

