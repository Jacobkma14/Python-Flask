import urllib.request
import json

# Function to get the number of people in space using OpenNotify API

def people_space():
  url="http://api.open-notify.org/astros.json"

  request=urllib.request.urlopen(url)
  result=json.loads(request.read())
  return result['number']