def getNearestBar(usLoc, bars: dict):
    distance = 1.0
    for bar in bars:
        newdist = ((float(bar['Longitude_WGS84']) - usLoc.longitude)**2 +
                   (float(bar['Latitude_WGS84']) - usLoc.latitude)**2)**0.5
        if newdist < distance:
            distance = newdist
            nearestBar = bar
    return nearestBar, distance
