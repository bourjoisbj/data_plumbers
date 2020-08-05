from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark import SparkContext
from collections import namedtuple
from pyspark.sql import SparkSession
import random
import re 


# Create a session if not existent otherwise get it
session = SparkSession.builder.appName("SparkSQLCount").getOrCreate()

sc = SparkContext.getOrCreate()

# Open window for streaming every 5s
ssc = StreamingContext(sc, 5)

fields = ("ID","Hashtag", "WordCount", "WordLength" )
Tweet = namedtuple( 'Tweet', fields )

# This function creates dataframes for each RDD in the session
# and call SQLtransform to load dataframes in SQL table
def transform( rdd ):
    if not rdd.isEmpty():
    	dataframes = session.createDataFrame(rdd)
    	SQLtransform(dataframes)
 

# This function is allows Spark to access the database and add rdd to the table
# sql_remote is the name of the database in SQL
# bj is the user that allows the user to access mySQL remotely
# TweetTable is the table we populate wuth dataframes

def SQLtransform(dataframes):
	dataframes.show()
	dataframes.write.format("jdbc")\
	.mode("overwrite")\
	.option("url", "jdbc:mysql://localhost:3306/sql_remote") \
	.option("dbtable", "TweetTable") \
	.option("user", "bj") \
	.option("password", "Welcome2BB") \
	.option("driver", "com.mysql.jdbc.Driver") \
	.save()

# Streaming from twitFlumSprk1 directory in HDFS 
lines = ssc.textFileStream("hdfs://localhost:9000//twitFlumSprk1")

# Transformation of data by mapping, filtering and reducing
counts = lines.flatMap( lambda l: l.split( " " ))\
	.filter( lambda w: w.lower().startswith("#") )\
	.map(lambda w: w.replace('#',''))\
	.map(lambda w: w.lower())\
	.filter(lambda w: re.sub(r'[^a-z]+', '', w))\
	.filter(lambda w: re.sub(r'[^\x00-\x7F]+',' ', w))\
	.filter(lambda w: len(w)>1)\
	.map( lambda w: ( w, 1 ) )\
	.reduceByKey( lambda x, y: x + y )\
	.map( lambda record: Tweet( random.randint(1,100000) ,record[0], record[1], len(record[0]) ) )\
	.foreachRDD(lambda l: transform(l))

ssc.start()
ssc.awaitTermination()

# spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.4 SparkSql.py
