from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from collections import namedtuple
from pyspark import SparkContext
from json import loads
import json


def handle_rdd(rdd):                                                                                                    
    if not rdd.isEmpty():                                                                                               
        global ss                                                                                                       
        dataframes = ss.createDataFrame(rdd, schema=['designation','label', 'quantity', 'unit'])                                                
        dataframes.show()                                                                                                       
        dataframes.write.saveAsTable(name='default.foodInfo', format='hive', mode='append')  


sc = SparkContext.getOrCreate()
SSC = StreamingContext(sc, 5)


fields = ("designation", "label", "quantity", "unit")
mytuple = namedtuple("nutrient", fields)

ks = KafkaUtils.createStream(scc, 'localhost:2181', 'sparkHive', {'APISparkHive':1})
res = ks.map(lambda l: jsons.loads(l[1]))\
        .map(lambda l: json.loads(x))\
        .flatMap(lambda l: l['label'], ['quantity'], ['unit'])\
        .map(lambda y: mytuple( y['designation'], y['label'], y['quantity'], y['unit']))\
        .foreachRDD(lambda l: handle_rdd(l))

                   
ssc.start()                                                                                                             
ssc.awaitTermination()

################################################################################################
# spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.4 API_SparkHive.py
################################################################################################
