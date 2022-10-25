import os
import csv

files = ["BERT-CNN-FBRO_0.844_50.h5.manual.csv",
         "BERT-CNN-TRANSF_0.819_120.h5.manual.csv"]


texts = []
trueLabels = []

fd = open(files[0], "r")
reader = csv.reader(fd)
next(reader)

for row in reader:
    texts.append(row[0])
    trueLabels.append(row[2])
fd.close()

content = []
for file in files:
    fd = open(file, "r")
    reader = csv.reader(fd)
    next(reader)

    currContent = []
    for row in reader:
        currContent.append(row[1])
    
    content.append(currContent)

    fd.close()

fd = open("manual.csv", "w")
writer = csv.writer(fd)
writer.writerow(["text", "cnnFBRO", "cnnTRANSF", "trueLabel"])
for text, trueLabel, cnnFBRO, cnnTRANSF in zip (texts, trueLabels, content[0], content[1]):
    writer.writerow([text, cnnFBRO, cnnTRANSF, trueLabel])

fd.close()