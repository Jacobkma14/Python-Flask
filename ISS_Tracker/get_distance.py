from geopy.distance import geodesic

def dist(lat1, lon1, lat2, lon2):
    """Calculate the distance between two points on Earth."""
    loc1 = (lat1, lon1)
    loc2 = (lat2, lon2)
    return geodesic(loc1, loc2).km
