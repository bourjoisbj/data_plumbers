from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from collections import namedtuple
from pyspark import SparkContext
from json import loads
import json


# Function for that create schema for database by transforming its RDD
# argument into dataframes with appropriate fields for storage in Hive
def handle_rdd(rdd):                                                                                                    
    if not rdd.isEmpty():                                                                                               
        global session                                                                                                    
        df = session.createDataFrame(rdd, schema=['property_id', 'listing_id', 'prop_type', 'prop_status', 'beds_max', 'baths_max', 'listing_status', 'price_min', 'price_max',\
        'rank', 'city'])
        dataframes = df.orderBy('price_max')
        dataframes.show()                                                                                                       
        dataframes.write.saveAsTable(name='default.realtorInfo', format='hive', mode='append')


# Set system for connnection of spark and the metastore
SparkContext.setSystemProperty("hive.metastore.uris", "thrift://localhost:9083")

# Create a Spark session if not existent otherwise get the existent session
session = SparkSession.builder.appName("SparkHiveStore").enableHiveSupport().getOrCreate()

sc = SparkContext.getOrCreate()
ssc = StreamingContext(sc, 20)


# Initialization of dataframes fields and table headers
fields = ('property_id', 'listing_id', 'prop_type', 'prop_status', 'beds_max', 'baths_max', 'listing_status', 'price_min', 'price_max',\
 'rank', 'city')

mytuple = namedtuple('prop_data', fields)
# , 'sqft_min', 'sqft_max'

# Streaming with Spark from Kafka through port 2181 that have a topic with 2 partitions
ks = KafkaUtils.createStream(ssc, 'localhost:2181', 'spark-streaming-consumer', {'RealtorStream':1})
try:
        res = ks.map(lambda l: json.loads(l[1]))\
                .map(lambda l: json.loads(l))\
                .map(lambda y: mytuple( y['property_id'], y['listing_id'], y['prop_type'], y['prop_status'], y['community']['beds_max'], \
                        y['community']['baths_max'], y['listing_status'], y['community']['price_min'], y['community']['price_max'], \
                        int(y['rank']), y['address']['city'] ))\
                .foreachRDD(lambda l: handle_rdd(l))

except:
        print('missing data')
        pass

# Strart the context                
ssc.start()   
ssc.awaitTermination()                                                                                                           

########################################################################################################
# spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.4 RealtorAPI_Transform.py
########################################################################################################