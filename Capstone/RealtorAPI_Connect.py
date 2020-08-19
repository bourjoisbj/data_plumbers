from kafka import KafkaProducer
from time import sleep
from json import dumps
import requests
import json


# # Define Kafka producer port
producertest = KafkaProducer(bootstrap_servers=['localhost:9099'], value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# API key for connection
# Try to catch exception in case of error
try:
	myheaders = {
		"x-rapidapi-host": "realtor.p.rapidapi.com",
		"x-rapidapi-key": "API Key",
		"useQueryString": 'true'
	}

	# Parameter initialization
	myquery = {
		"sort": "relevance",
		"city": "New York City",
		"state_code": "NY",
		"limit": "200",
		"offset": "0"
	}

	# Resquest data from API
	# print(type(myquery))
	req = requests.get("https://realtor.p.rapidapi.com/properties/v2/list-for-rent", headers = myheaders, params = myquery)

# Catch exception if connection is NOT made
except requests.exceptions.ConnectionError:
    r.status_code = "Connection refused"


# Parsing data
data = req.json() 
data_Parsed = data['properties']

# Printing the 1st element of the dict of json
print(data_Parsed[0])


# Producer sends data to the broker: this is sent using a loop because
# the message is a collection of json, needed to be sent one at the time
for message in data_Parsed:
	producertest.send("RealtorStream", json.dumps(message))
	sleep(1)


#############################################  PRINNTING  #################################################

# Another way to print data in a clearly readable format
# print() |tr '}' '\n'|tr ',' '\n'|more
# print(json.dumps(data_Parsed, indent=4))       
# print(json.dumps(data['properties'][1]['community'], indent=4))
