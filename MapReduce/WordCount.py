from functools import reduce
import re
# %time

f = open("Shakespeare.txt", "r")

# Save the file in lower character in a string myBigData
myBigData = f.read().lower()

myCleanList = re.split( ' |\n|:|"|;|<|\(|\)|\.|\'|!|\?|,|>', myBigData)
wordList = []

# Creaing a list of words with no duplicates
for w in myCleanList:
    if w not in wordList:
        wordList.append(w)

# Output each word with its count
for w in range(0, len(wordList)):
    print(wordList[w], myBigData.count(wordList[w]))


# for x in f:
# 	myBigData.append(x)

# myList = list( map( lambda l : l.lower(), myBigData) )

# # print(myList)

# noDuplicateList = list( dict.fromkeys( myList)) 

# mapping = list( map( lambda e: (e, 1) ,myBigData))
