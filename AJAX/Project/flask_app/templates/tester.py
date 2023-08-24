import requests
import json

response = requests.get("http://www.thecocktaildb.com/api/json/v1/1/random.php")
result = response.json()

print(result)