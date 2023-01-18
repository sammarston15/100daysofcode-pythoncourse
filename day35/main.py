import os
import requests
from twilio.rest import Client

weather_api_key = os.getenv('WEATHER_API_KEY')
base_url = os.getenv('WEATHER_BASE_URL')
twilio_sid = os.getenv('TWILIO_SID')
twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')


params = {
    "appid": weather_api_key,
    "lat": 39.738449,
    "lon": -104.984848,
    "exclude": "current,minutely,daily"

}

response = requests.get(base_url, params=params)
response.raise_for_status()
data = response.json()

will_rain = False

for item in data['hourly'][:12]:
    if int(item['weather'][0]['id']) > 700:
        will_rain = True

if will_rain:
    client = Client(twilio_sid, twilio_auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring your Umbrella.",
                     from_='+14196644749',
                     to='+13852512971'
                 )
    
    print(message.status)