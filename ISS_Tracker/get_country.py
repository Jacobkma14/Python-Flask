import urllib.request 
import requests

def country(name):
    url = f"https://restcountries.com/v3.1/alpha/{name}""}"
    response = urllib.request.urlopen(url)
    result=json.loads(response.read())
    print(result)
    return result

