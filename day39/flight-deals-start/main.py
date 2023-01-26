#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch


def main():
    data_manager = DataManager()
    flight_search = FlightSearch()
    sheet_data = data_manager.get_destination_data()
    print(sheet_data)

    for item in sheet_data:
        if item['iataCode'] == "":
            item['iatacode'] = flight_search.get_destination_code(city_name=item['city'])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()





if __name__ == "__main__":
    main()