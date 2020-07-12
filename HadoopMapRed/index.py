from functools import reduce
import re

f = open("test.txt", "r")

# Save the file in lower character in a string myBigData
myBigData = f.read().lower()

myCleanList = re.split( ' |\n|:|"|;|<|\(|\)|\.|\'|!|\?|,|>', myBigData)
wordList = []

# Creaing a list of words
for w in myCleanList:
    wordList.append(w)

# Mapping the list 
# myList = list( map( lambda l :(l, 1), wordList) )
# result = list( map( lambda l :(l, 1), wordList) )

# noDuplicateList = list( dict.fromkeys( myList)) 

# Reducing the list
# result = reduce( lambda x, y : if )

# Output each word with its count
# for w in result:
#     print(first[w], second[w])

