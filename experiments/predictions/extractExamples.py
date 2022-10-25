import os
import csv

files = ["BERT_FBRO_0.755_16_30_32.h5.predictions.csv",
         "BERT_TRANSF_0.755_128_120_128.h5.predictions.csv",
         "BERT-CNN-FBRO_0.844_50.h5.predictions.csv",
         "BERT-CNN-TRANSF_0.819_120.h5.predictions.csv",
         "SVM_predictions.csv",
         "SVM_predictions_transf.csv"]


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

fd = open("discussions.csv", "w")
writer = csv.writer(fd)
writer.writerow(["text",  "cnnFBRO", "cnnTRANSF", "trueLabel",])
for text, trueLabel, bertFBRO, bertTRASNF, cnnFBRO, cnnTRANSF, SVM, SVMTRANSF in zip (texts, trueLabels, content[0], content[1], content[2], content[3], content[4], content[5]):
    nrdifs = 0

    # if bertFBRO != trueLabel:
    #     nrdifs += 1

    # if bertTRASNF != trueLabel:
    #     nrdifs += 1

    if cnnFBRO != trueLabel:
        nrdifs += 1

    if cnnTRANSF != trueLabel:
        nrdifs += 1
    
    # if SVM != trueLabel:
    #     nrdifs += 1

    # if SVMTRANSF != trueLabel:
    #     nrdifs += 1


    if nrdifs >= 1:
        writer.writerow([text, cnnFBRO, cnnTRANSF, trueLabel])

fd.close()