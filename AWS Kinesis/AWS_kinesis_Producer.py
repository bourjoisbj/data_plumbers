import boto3
import requests
from json import dumps
import json
import os

client = boto3.client(
    'kinesis',
    region_name='us-east-2',
    aws_access_key_id = <your key>,
    aws_secret_access_key = <your key>
)

myheaders = {
        "x-rapidapi-host": "yelp-com.p.rapidapi.com",
        "x-rapidapi-key": "API key",
        "useQueryString": 'true'
}

req = requests.get('https://yelp-com.p.rapidapi.com/business/DAiqwrmv19Uv-I1bOoAJCQ', headers=myheaders)
data = req.json()
print(data)


client.put_record(StreamName='myStream', Data=json.dumps(data).encode('utf-8'), PartitionKey='1')

    
