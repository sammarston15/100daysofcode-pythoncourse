import os
import requests
from datetime import datetime
import json

GENDER = "male"
WEIGHT = 96.16
HEIGHT = 175.26
AGE = 25

NUTRI_APP_ID = os.getenv('NUTRI_APP_ID')
NUTRI_API_KEY = os.getenv('NUTRI_API_KEY')
nutri_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"





""" POST NUTRI API TO GET EXERCISE CALORIES """
query_info = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY,
}

params = {
 "query": query_info,
 "gender":GENDER,
 "weight_kg": WEIGHT,
 "height_cm": HEIGHT,
 "age": AGE
}

response = requests.post(url=nutri_exercise_endpoint, json=params, headers=headers) # post requests need the `json` keyword in the function and NOT `params` for you to have success
# response.raise_for_status()
exercise_data = response.json()
print("   ")
print("   ")
print(json.dumps(exercise_data, indent=4))
print("   ")
print("   ")




""" POST TO SHEETY API TO ADD EXERCISE TO YOUR GOOGLE SHEET """
sheety_post_endpoint = "https://api.sheety.co/82b93e3605e19854564fe47a3c8e3f6d/workoutTracking/workouts"

for exercise in exercise_data['exercises']:
    sheety_params = {
        "workout": {
            "date": datetime.now().strftime("%m/%d/%y"),
            "time": datetime.now().strftime("%I:%M:%S %p"),
            "exercise": exercise['name'].title(),
            "duration (mins)": f"{exercise['duration_min']}",
            "calories": exercise['nf_calories']
        }
    }

    sheety_headers = {
        "Authorization": f"Basic {os.getenv('SHEETY_AUTH')}"
    }

    sheety_response = requests.post(sheety_post_endpoint, json=sheety_params, headers=sheety_headers)
    print("   ")
    print("   ")
    print(sheety_response.json())