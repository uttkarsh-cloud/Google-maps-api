import location
from math import sin, cos, sqrt, atan2, radians

class places:
    def __init__(self, listofplaces, listofplaces2):
        self.locations = []
        self.locations2 = []
        for place in listofplaces:
            try:
                self.locations.append(location.location(place['geometry'], name=place['name']))
            except:
                print('error')
        for place in listofplaces2:
            try:
                self.locations2.append(location.location(place['geometry'], name=place['name']))
            except:
                print('error')
    def printThreeClosest(self):
        closest = []
        for i in range(0, len(self.locations)):
            loc1 = self.locations[i]
            for i2 in range(0, len(self.locations2)):
                loc2 = self.locations2[(i2)]
                d = self.distance(loc1, loc2)
                closest.append([d, [loc1, loc2]])
        sCloses = sorted(closest, key=places.getKey)
        c = 0
        for i in sCloses:
            if c == 3:
                break
            print("Pair #" + str(c))
            print(i[1][0].toPretty())
            print(i[1][1].toPretty())
            c += 1

    def distance(self, loc1, loc2):
        lat1 = radians(loc1.lat)
        lon1 = radians(loc1.lng)
        lat2 = radians(loc2.lat)
        lon2 = radians(loc2.lng)

        R = 6373.0

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = (sin(dlat / 2)) ** 2 + cos(lat1) * cos(lat2) * (sin(dlon / 2)) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c

        return distance
    def getKey(item):
        return item[0]