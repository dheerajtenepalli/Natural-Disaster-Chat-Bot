#In Future I plan to use geolocation and Maps Javascript API from google to further narrow down the accuracy.
"""
Here is the entire code for Google geolocation. 
Note_1 : Not using google only because of the cost.Also there is a quota limit of one loading per day which is very restricting.
Important_Note_2 : I have also written down code to display user location on Maps using Maps Javascript API. Not using it because of cost. 

Code for Google javascript can be found in templates/example.html and run.py

******Code********
import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyDxAdPo7k_9P3oHbnBun8AJXcZLMGFkV8A')
geocode_result = gmaps.geolocate()
print(geocode_result)

"""

# All Location related functions
import geocoder
from math import sin, cos, sqrt, atan2, radians
from geopy.geocoders import Nominatim
import yweather

client = yweather.Client()

def get_lat_long():
	g = geocoder.ip('me')
	print(g.latlng)
	return g.latlng

def distance(lat1,lat2,long1,long2):
	# approximate radius of earth in km
	R = 6373.0

	lat1 = radians(lat1)
	lon1 = radians(long1)
	lat2 = radians(lat2)
	lon2 = radians(long2)

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = R * c

	print("Result:", distance)
	return distance 
def get_woeid(city):
	woeid = client.fetch_woeid(city)
	print("My Woeid is ",woeid)
	return 	woeid
	
def get_address_for_lat_long(latitude,longitude):
	string_for_reverse_location = str(latitude)+","+ str(longitude) 
	geolocator = Nominatim(timeout=3,user_agent="Elizabeth")
	location = geolocator.reverse(string_for_reverse_location)
	print("Raw",location.raw['address']['city'])
	try:	
		woeid = client.fetch_woeid(location.raw['address']['city'])
	except Exception as e:
		print("Not Found")
		return  location.raw['address']['city'], location.address,23424977 
	 
	return  location.raw['address']['city'], location.address,woeid

#output = get_lat_long()
#city,address= get_address_for_lat_long(output[0], output[1])


