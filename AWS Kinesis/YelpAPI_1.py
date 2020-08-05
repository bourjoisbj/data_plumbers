import http.client
conn = http.client.HTTPSConnection("yelp-com.p.rapidapi.com")
headers = {
    'x-rapidapi-host': "yelp-com.p.rapidapi.com",
    'x-rapidapi-key': "your key"
    }
conn.request("GET", "/business/DAiqwrmv19Uv-I1bOoAJCQ", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
