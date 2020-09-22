import json

class location:
    def __init__(self, jstring, name=''):
        self.lat = jstring["location"]["lat"]
        self.lng = jstring["location"]["lng"]
        self.name = name

    def toDict(self):
        return {"lat" : self.lat, "lng" : self.lng}

    def toPretty(self):
        return {"lat" : self.lat, "lng" : self.lng, "name" : self.name}
