#Name: Nijil K Babu
#PGID: 71721084

#Question 5

fileName = "Random generated file.txt"

def getWordsInUpperCase(fileName)
    file = open(fileName, "r")
    
    wordArr = []
    for line in file: 
        newLine = string.translate(line, None, string.punctuation)
        newLine = string.upper(newLine)
        newLineArr = newLine.split()
        wordArr.append(newLineArr)
    return wordArr


getWordsInUpperCase(fileName)
        