import urllib.request
import json
def iss_loc():
    # URL to get ISS location data
    url = "http://api.open-notify.org/iss-now.json"

    # Make the request to get the data
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())

# Extract latitude and longitude from the result
    lat = result['iss_position']['latitude']
    lon = result['iss_position']['longitude']
    print(f"https://www.google.com/maps/place/" + lat +"+" +lon)
    return lat, lon
    
