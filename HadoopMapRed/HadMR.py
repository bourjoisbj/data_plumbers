from collections import Counter
from functools import reduce
import re

f = open("/Users/abdelbileomon/Desktop/Enhance IT/data_plumbers/HadoopMapRed/test.txt", "r")

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
counter = Counter(wordList)
print zip(counter.keys(), counter.values())

# Another alternative
# print Counter(wordList).items()






# noDuplicateList = list( dict.fromkeys( myList)) 
