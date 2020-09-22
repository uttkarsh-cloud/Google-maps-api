import googlemaps
import googlemaps.places
import googlemaps.geolocation
import location
import places

def loadApiKey(filename):
    with open(filename) as file:
        return file.readline()

#this is so bad
apikey = loadApiKey('key.txt')

gmps = googlemaps.Client(key=apikey)

def main():
    global gmps
    loc1 = input("Enter location #1: ")
    loc2 = input("Enter location #2: ")
    distance = int(input('Radius you want to search in miles'))

    response = googlemaps.geolocation.geolocate(
        client = gmps,
        consider_ip=True)

    loc = location.location(response)

    placesNearby = googlemaps.places.places_nearby(client= gmps,
                                    keyword=loc1,
                                    location=loc.toDict(),
                                    radius=int(distance * 1609))

    placesNearby2 = googlemaps.places.places_nearby(client= gmps,
                                    keyword=loc2,
                                    location=loc.toDict(),
                                    radius=int(distance * 1609))


    places1 = places.places(placesNearby["results"], placesNearby2['results'])
    places1.printThreeClosest()

if __name__ == '__main__':
    main()