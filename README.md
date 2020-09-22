# PlaceFinder
PlaceFinder is a simple python program that takes advantage of the Google Maps API.  This program allows you to enter two types of places and a radius.  Based on your location it will return three pairs of places that are closest to one another.

## Running
1.  To run this program you will need python3 and the <a href="https://github.com/googlemaps/google-maps-services-python"> googlemaps </a> api.
2.  You will also need to create a file in the root directory called key.txt, this file must contain a single line with the api key provided by google.  
3.  The services that you must have enabled for the api key are:
    -  Google Places API Web Service.
    -  Google Maps Geolocation API.
4. To run use:  ```python3 main.py```
