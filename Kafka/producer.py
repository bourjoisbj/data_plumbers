import json
from kafka import KafkaProducer
from time import sleep
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9099'])
f = open('/home/fieldemploye/opt/Shakespeare.txt', 'r')
lineList = f.readlines()

for x in range(len(line_list)):
	producer.send('data',json.dumps(lineList[x]).encode('utf-8'))
	sleep(1)
	