import csv
import os

anonUsers = {}
currUserId = 1

writeFile = open("finalDataset.csv", "w")
writer = csv.writer(writeFile)
writer.writerow(["sender", "no_reacts", "text", "label"])

readFile = open("./originalAnnotatedDataset.csv", "r")
reader = csv.reader(readFile)
next(reader)

for row in reader:
    if(row[3] == "DROP" or row[3] == ""):
        continue

    sanitizedRow = []

    # ANON USERS
    if (row[0] not in anonUsers):
        anonUsers[row[0]] = '$USER'+str(currUserId).rjust(4, '0')
        currUserId += 1
    sanitizedRow.append(anonUsers[row[0]])

    # NUMBER OF REACTS + TEXT
    sanitizedRow.append(row[1])
    sanitizedRow.append(row[2])

    # ONLY 1 LABEL
    if (row[3] == "OTHER"):
        sanitizedRow.append(row[3])
    else:
        sanitizedRow.append(row[4])

    writer.writerow(sanitizedRow)

writeFile.close()
readFile.close()