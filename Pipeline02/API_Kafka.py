from __future__ import absolute_import
from kafka import KafkaClient
from kafka import KafkaProducer
from time import sleep
from json import dumps
import requests
import json


# # Define Kafka producer port
producertest = KafkaProducer(bootstrap_servers=['localhost:9099'])

# API key for connection
myheaders = {
   	"x-rapidapi-host": "edamam-edamam-nutrition-analysis.p.rapidapi.com",
	"x-rapidapi-key": "your key",
	"useQueryString": 'true'
}

# Parameter initialization
myquery = {
    	"ingr": "1 large apple"
}

# Resquest data from API
req = requests.get('https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-data', headers = myheaders, params = myquery)
data = req.json()
# print(data)

new = data["totalNutrients"]
# print(new)

# Producer sends data to the broker
producertest.send("APISparkHive", json.dumps(data))
