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
myList = list( map( lambda l :(l, 1), wordList) )

# Reducing the list
result = reduce( lambda (x,y) : if x == , myList)

# Output each word with its count
# for w in result:
print(tuple(result))

