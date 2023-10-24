
import requests

def get_weather(apikey, city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    parameter = {"q": city, "appid": apikey"}
    
    resonse = requests.get
