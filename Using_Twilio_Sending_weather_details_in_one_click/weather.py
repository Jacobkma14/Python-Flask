import urllib.request 
import json

# Function to get weather information using OpenWeather API

def get_weather(city):
  api_key = "0c064bf24b52b7b932f6a82713a2f773" 
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
  request=urllib.request.urlopen(url)
  result=json.loads(request.read())
  return result['main']['temp']
  