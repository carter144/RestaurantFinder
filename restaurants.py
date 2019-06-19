

import googlemaps
from datetime import datetime
import requests
import argparse
import operator
import json
import random

class Restaurants:
    def __init__(self, lat, longitude, radius, keyword, key, rand):
        self.lat = lat
        self.long = longitude
        self.radius = radius
        self.keyword = keyword #optional
        self.key = key
        self.rand = rand

    def buildQuery(self):
        base = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
        location = "&location=" + self.lat + "," + self.long
        radius = "&radius=" + self.radius
        type_param = "&type=restaurant"
        keyword = ""
        if self.keyword is not None:
            keyword = "&keyword=" + self.keyword
        
        key = "&key=" + self.key




        self.url = base + location + radius + type_param + keyword + key
        

    def getResults(self):
    	r = requests.get(self.url)
    	self.results = r.json()["results"]

    	if (self.rand):
    		index = random.randint(0, len(self.results) - 1)
    		cleaned_object = self.parseObject(self.results[index])
    		print(cleaned_object)
    		return

    	self.results.sort(key=operator.itemgetter('rating'), reverse=True)
    	
    	for i in range(5):
    		print(self.parseObject(self.results[i]))



    def parseObject(self, data):

    	name = data["name"]
    	rating_total = data["user_ratings_total"]
    	rating = data["rating"]
    	try:
    		price = data["price_level"]
    	except:
    		price = "-1"
    	address = data["vicinity"]


    	return {
	    	"Name": name,
	    	"Rating": rating,
	    	"Number of Ratings": rating_total,
	    	"Price": price,
	    	"Address": address
    	}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', help='please enter the radius in meters: -r [25000]', required=True)
    parser.add_argument('-k', help='please enter a keyword to search for: -k [pizza in newyork]', required=False)
    parser.add_argument('-random', help='please enter a keyword to search for: -random [Y/N]', required=False)
    args = parser.parse_args()
    radius = args.r
    keyword = args.k
    rand = args.random
    if rand is not None:
    	rand = True
    else:
    	rand = False

    key = '<YOUR API KEY HERE>'
    restaurants = Restaurants('37.62569530416217', '-77.55075216293335', radius, keyword, key, rand)
    restaurants.buildQuery()
    restaurants.getResults()