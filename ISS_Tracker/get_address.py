import urllib.request
import requests
import json


def address(lat, lon):
    url = f"https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={lat}&longitude={lon}&localityLanguage=en"  
    # Open the URL and read data
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    print(result)
    return result
