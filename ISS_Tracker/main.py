from flask import Flask, render_template
from get_iss import iss_loc
from get_weather import get_weather
from get_address import address
from get_distance import dist
import requests

app = Flask(__name__)

def get_flag_url(country_code):
    response = requests.get(f"https://restcountries.com/v3.1/alpha/{country_code}")
    data = response.json()
    return data[0]["flags"]["png"]

@app.route('/')
def index():
    # Where is the space station
    data = iss_loc()
    lat, lon = data[0], data[1]

    # Weather
    weather = get_weather(lat, lon)
    temp_c = round(weather["main"]["temp"] -273.15, 2)
    desc = weather["weather"][0]['description']

    # Distance from the ISS
    distance = dist(lat, lon, 46.4915458, -80.9947947)

    # Address reverse geolocation
    addr = address(lat, lon)
    country_name = addr["countryName"]
    country_code = addr["countryCode"]

    if country_code == "":
        country_name = 'The ISS is over water'
        flag_url = "No flag available"
    else:
        flag_url = get_flag_url(country_code)

    return render_template(
        'index.html',
        lat=lat,
        lon=lon,
        weather_description=desc,
        temperature=temp_c,
        country=country_name,
        flag_url=flag_url,
        distance=distance
    )
app.run(host='0.0.0.0', port=8080)
