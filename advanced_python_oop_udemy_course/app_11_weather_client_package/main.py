import os

from dotenv import load_dotenv
from sunnyday import Weather


load_dotenv()


API_KEY = os.getenv("APIKEY")
lat = 22.781186
lon = -103.559961
weather = Weather(api_key=API_KEY, lat=lat, lon=lon)

print(weather.next_12h())
print("*"*24)
print(weather.next_12h_simplified())