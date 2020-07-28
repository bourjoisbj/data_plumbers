from pyspark import SparkContext

if __name__ == "__main__"
    sc = SparkContext("local[2]", "WordCount")
    sc.setLogLevel("ERROR")
    
    lines = sc.textFile("/home/fieldemploye/opt/Shakespeare.txt")
    words = lines.flatMap(lambda l: l.split(" "))
    
    WordCounts = words.countByValue()
    for word, count in WordCounts.items():
        print("{} , {}".format(word, count))
