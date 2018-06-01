import calculations
from upload_data import getBarsDB
import json

bars = json.loads(getBarsDB())

def getNearestBar(userLocation):
    bar, dist = calculations.getNearestBar(userLocation, bars)
    return [bar['Name'], bar['Address'], bar['PublicPhone'][0]['PublicPhone'],
            bar['Latitude_WGS84'], bar['Longitude_WGS84'], int(dist * 1500) + 1]