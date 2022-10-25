from email import header
import plotly.express as px
import csv
import os

studiesPath = [
               "./BERT_SIMPLE/FBRO/studies/FBROstudy-BERT-SIMPLE.csv",
               "./BERT_CNN/FBRO/studies/FBROstudy-BERT-CNN.csv",
               "./BERT_SIMPLE/TRANSF/studies/TRANSFstudy-BERT-SIMPLE.csv",
               "./BERT_CNN/TRANSF/studies/BERT-CNN-TRANSFstudy.csv"
            ]


for studyPath in studiesPath:
    file = open(studyPath, "r")
    reader = csv.reader(file)
    header = next(reader)

    denseSize = []
    learningRate = []
    batchSize = []
    tokMaxLen = []
    fgLoss = []
    fgAccuracy = []
    fgPrec = []
    fgRecall = []
    fgF1Micro = []
    fgF1Macro = []

    cgAccuracy = []
    cgPrecision = []
    cgRecall = []
    cgF1 = []

    for row in reader:
        # if (float(row[4]) < 0.7):
        #     continue
        denseSize.append(int(row[0]))
        learningRate.append(float(row[1]))
        batchSize.append(int(row[2]))
        tokMaxLen.append(int(row[3]))
        fgLoss.append(float(row[4]))
        fgAccuracy.append(float(row[5]))
        fgPrec.append(float(row[6]))
        fgRecall.append(float(row[7]))
        fgF1Micro.append(float(row[8]))
        fgF1Macro.append(float(row[9]))
        cgAccuracy.append(float(row[10]))
        cgPrecision.append(float(row[11]))
        cgRecall.append(float(row[12]))
        cgF1.append(float(row[13]))

    pathSplit = studyPath.split("/")

    fig = px.parallel_coordinates({"denseSize": denseSize, "learningRate":learningRate, "batchSize":batchSize, "tokMaxLen":tokMaxLen, "FGAccuracy":fgAccuracy}, 
                                dimensions=['denseSize', 'learningRate', 'batchSize', 'tokMaxLen', 'FGAccuracy'],
                                color="FGAccuracy",
                                color_continuous_scale=px.colors.diverging.Portland,
                                title="Fine Grained Accuracy for " + pathSplit[1] + " " + pathSplit[2])
    fig.show()

    fig = px.parallel_coordinates({"denseSize": denseSize, "learningRate":learningRate, "batchSize":batchSize, "tokMaxLen":tokMaxLen, "CGAccuracy":cgAccuracy}, 
                                dimensions=['denseSize', 'learningRate', 'batchSize', 'tokMaxLen', 'CGAccuracy'],
                                color="CGAccuracy",
                                color_continuous_scale=px.colors.diverging.Portland,
                                title="Coarse Grained Accuracy for " + pathSplit[1] + " " + pathSplit[2] )
    fig.show()


    # fig = px.parallel_coordinates({"learningRate":learningRate, "batchSize":batchSize, "seed":seed, "fgF1Micro":fgF1Micro}, 
    #                             dimensions=['learningRate', 'batchSize', 'seed', 'fgF1Micro'],
    #                             color="fgF1Micro",
    #                             color_continuous_scale=px.colors.diverging.Portland,
    #                             title="Fine Grained Accuracy for " + pathSplit[1] + " " + pathSplit[2])
    # fig.show()

    # fig = px.parallel_coordinates({"learningRate":learningRate, "batchSize":batchSize, "seed":seed, "cgF1":cgF1}, 
    #                             dimensions=['learningRate', 'batchSize', 'seed', 'cgF1'],
    #                             color="cgF1",
    #                             color_continuous_scale=px.colors.diverging.Portland,
    #                             title="Coarse Grained Accuracy for " + pathSplit[1] + " " + pathSplit[2] )
    # fig.show()