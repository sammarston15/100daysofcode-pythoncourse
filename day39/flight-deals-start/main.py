#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch


def main():
    data_manager = DataManager()
    flight_search = FlightSearch()
    sheet_data = data_manager.get_destination_data()

    ORIGIN_CITY_IATA = "LON"

    # update IATA code in your database (google sheet) if empty
    for item in sheet_data:
        if item['iataCode'] == "":
            item['iataCode'] = flight_search.get_destination_code(city_name=item['city'])

            data_manager.destination_data = sheet_data
            data_manager.update_destination_data()

    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    # search for available flights for each destination listed in your db (google sheet)
    for destination in sheet_data:
        flight = flight_search.check_flights(
            origin_city_code=ORIGIN_CITY_IATA,
            destination_city_code=destination['iataCode'],
            from_time=tomorrow,
            to_time=six_month_from_today
        )





if __name__ == "__main__":
    main()