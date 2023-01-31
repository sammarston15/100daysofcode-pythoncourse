import requests
import json

sheety_get_endpoint = "https://api.sheety.co/82b93e3605e19854564fe47a3c8e3f6d/flightDeals/prices"
sheety_post_endpoint = "https://api.sheety.co/82b93e3605e19854564fe47a3c8e3f6d/flightDeals/prices"
sheety_put_base_endpoint = "https://api.sheety.co/82b93e3605e19854564fe47a3c8e3f6d/flightDeals/prices" # object ID is just the row number according to the docs: https://sheety.co/docs/requests.html

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheety_response = requests.get(sheety_get_endpoint)
        sheet_data_prices = sheety_response.json().get('prices', None)
        self.destination_data = sheet_data_prices
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city['iataCode']
                }
            }
            response = requests.put(
                url=f"{sheety_put_base_endpoint}/{city['id']}",
                json=new_data
            )
            if response.status_code == 200:
                print('data updated.')

        # print the updated data once all data is done updating
        print(self.get_destination_data())
    