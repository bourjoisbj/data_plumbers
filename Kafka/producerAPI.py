
from time import sleep
from kafka import KafkaProducer
from json import dumps
import json
import requests

producer = KafkaProducer(bootstrap_servers = ['localhost:9099'], 
						 value_serializer = lambda l: 
						 dumps(l).encode('utf-8'))
# req.query({
# 	"title": "Spaghetti Aglio et Olio"
# });

headers = {
	"x-rapidapi-host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
	"x-rapidapi-key": "470324e088msh384fa183976ea5bp1ced01jsnbcb05ef02e91",
	"useQueryString": 'true'
}

req = requests.get('https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/guessNutrition', headers = headers)

response = req.text

for i in range(1):
	producer.send('KafkaAPI', json.dumps(response))
	print("GREAT")

producer.send('KafkaAPI', json.dumps(response).encode('utf-8'))
