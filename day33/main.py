# IMCOMPLETE!!

import requests
from datetime import datetime

MY_LAT = 32.222607
MY_LONG = -110.974709

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
longitude = float(data['iss_position']['longitude'])
latitude = float(data['iss_position']['latitude'])
iss_position = (latitude, longitude)

# your position is within +5 or -5 degrees of the iss position


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

time_now = datetime.now()
