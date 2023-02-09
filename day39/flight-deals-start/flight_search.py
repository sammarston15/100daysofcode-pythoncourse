import requests
import os
from flight_data import FlightData

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


    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": KIWI_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(
            url=f"{KIWI_BASE_URL}/v2/search",
            headers=headers,
            params=query
        )

        try:
            data = response.json()['data'][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{KIWI_BASE_URL}/v2/search",
                headers=headers,
                params=query,
            )
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data['price'],
                origin_city=data['route'][0]['cityFrom'],
                origin_airport=data['route'][0]['flyFrom'],
                destination_city=data['route'][0]['cityTo'],
                destination_airport=data['route'][0]['flyTo'],
                out_date=data['route'][0]['local_departure'].split('T')[0],
                return_date=data['route'][1]['local_departure'].split('T')[0]
            )
            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data