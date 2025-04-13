import urllib.request
import json
OPENWEATHERMAP_API_KEY = "0c064bf24b52b7b932f6a82713a2f773"
def get_weather(lat, lon):
    
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHERMAP_API_KEY}"

 
    # Open the URL and read data
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())

    print(result)

    return result

