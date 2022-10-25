import csv
import os
import statistics
from time import sleep
from broadcastArhitecture import Comment

swearKeywordsFile = "swearKeywords"
facebookDataDir = "facebookData"
commentsInfoFile = "comments.csv"
broadcastInfoFile = "broadcast.csv"
dataSetName = "dataset.csv"
maxNumberOfPredecessors = 2
maxNumberOfSSuccessors = 4

def computeSwearKeywords():
    file = open (swearKeywordsFile, "r")
    keyWords = file.readlines()
    result = [key[:-1] for key in keyWords]
    file.close()
    return result

def sanitizeCommentText(text):
    romanianSpecialChars   = "ăâîțș"
    romanianToEnglishChars = "aaits"
    text = text.lower()

    for char in romanianSpecialChars:
        text = str.replace(text, char, romanianToEnglishChars[romanianSpecialChars.index(char)])
        
    text = str.replace(text, "-", "")
    return str.split(text)

def getRelativePathsToCommentsInfo():
    relativePathsToCommentsInfo = []
    facebookDataDirs = os.listdir(facebookDataDir)
    for dir in facebookDataDirs:
        pathToCommentsInfoFile = os.path.join(facebookDataDir, dir, commentsInfoFile)
        relativePathsToCommentsInfo.append(pathToCommentsInfoFile)
    return relativePathsToCommentsInfo

def isSwearComment(comment, keyWords):
    sanitizedTextAsList = sanitizeCommentText(comment.text)
    for key in keyWords:
        if key in sanitizedTextAsList:
            return True
    return False

def eligibleSwearComment(comment, keyWords, minLen, maxLen):
    sanitizedTextAsList = sanitizeCommentText(comment.text)
    commentLen = len(comment.text)
    for key in keyWords:
        if key in sanitizedTextAsList and commentLen <= maxLen and commentLen >= minLen:
            return True
    return False

def eligibleComment(comment, keyWords, minLen, maxLen):
    commentLen = len(comment.text)
    if commentLen <= maxLen and commentLen >= minLen:
        return True
    return False

def getPredecessors(comments, parentIdx, keyWords, mean, stdev, result):
    parentIdx -= 1
    res = []
    nr = 0
    while parentIdx >= 0:
        if eligibleComment(comments[parentIdx], keyWords,  mean - stdev, mean + stdev) and comments[parentIdx] not in result:
            res.append(comments[parentIdx])
            nr += 1
            if nr == maxNumberOfPredecessors:
                break
        parentIdx -= 1
    return res

def getSuccessors(comments, parentIdx, keyWords, mean, stdev, result):
    parentIdx += 1
    res = []
    nr = 0
    while parentIdx < len(comments):
        if eligibleComment(comments[parentIdx], keyWords,  mean - stdev, mean + stdev) and comments[parentIdx] not in result:
            res.append(comments[parentIdx])
            nr += 1
            if nr == maxNumberOfSSuccessors:
                break
        parentIdx += 1
    return res

def getStatistics(keyWords):
    relativePathsToCommentsInfo = getRelativePathsToCommentsInfo()

    nr = 0
    commentsLen = []
    for path in relativePathsToCommentsInfo:
        file = open(path, "r")
        reader = csv.reader(file)
        comments = []

        for row in reader:
            comments.append(Comment(row[0], row[1], 0, row[2]))

        for comment in comments:
            if isSwearComment(comment, keyWords):
                commentsLen.append(len(comment.text))
                nr += 1
        
    mean = statistics.mean(commentsLen)
    stdev = statistics.stdev(commentsLen)
    return [mean, stdev]

def getFinalListOfComments(keyWords, mean, stdev):
    relativePathsToCommentsInfo = getRelativePathsToCommentsInfo()

    result = []
    for path in relativePathsToCommentsInfo:
        file = open(path, "r")
        reader = csv.reader(file)
        comments = []
        for row in reader:
            comments.append(Comment(row[0], row[1], 0, row[2]))


        for comment in comments:
            if comment not in result and eligibleSwearComment(comment, keyWords,  mean - stdev, mean + stdev):
                neighbours = [comment]
                neighbours += getPredecessors(comments, comments.index(comment), keyWords, mean, stdev, result)
                neighbours += getSuccessors(comments, comments.index(comment), keyWords, mean, stdev, result)
                result += neighbours

    return result

def writeToCSV(comments, fileName):
    f = open (fileName, "w")
    writer = csv.writer(f)
    writer.writerow(["Sender", "NumberOfReacts", "Text"])
    for comment in comments:
        writer.writerow([comment.sender, str(comment.numberOfReacts), comment.text])
    f.close()

def computeDatasetComments(keyWords):
    statistics = getStatistics(keyWords)
    mean = int(statistics[0])
    stdev = int(statistics[1] / 2)

    print ("Min len for comment is " + str(mean - stdev))
    print ("Max len for comment is " + str(mean + stdev))

    finalListOfComments = getFinalListOfComments(keyWords, mean, stdev)
    finalSetOfComments = set(finalListOfComments)
    
    writeToCSV(finalListOfComments, dataSetName)

def main():
    keyWords = computeSwearKeywords()
    computeDatasetComments(keyWords)
    
if __name__ == "__main__":
    main()
