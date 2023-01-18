from urllib import request
import requests
import json

params = {
    "amount": 10,
    "type": "boolean",
    "category": 18 #computer science questions
}

response = requests.get("https://opentdb.com/api.php", params=params)
response.raise_for_status()
data = response.json()

question_data = data['results']



