import requests
from pprint import pprint

API_Key='fe5018bf6b2232ebf4b8f519f164ce3d'

city=input("Enter a city: ")

base_url="https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city
weather_data=requests.get(base_url).json()
pprint(weather_data)