import requests
import os

KIWI_API_KEY = os.getenv('KIWI_API_KEY')
KIWI_BASE_URL = "https://api.tequila.kiwi.com"



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def get_destination_code(self, city_name):
        headers = {
            "apikey": KIWI_API_KEY,
        }

        kiwi_params = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(
            url=f"{KIWI_BASE_URL}/locations/query",
            headers=headers,
            params=kiwi_params
        )
        response.raise_for_status()
        
        return response.json()['locations'][0]['code']