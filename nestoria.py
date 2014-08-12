#!/usr/bin/env python
 
import urllib2
import json
 
from collections import namedtuple

# HARCODED SEARCH STRING - WILL REMOVE LATER 
NESTORIA_API_URL = "http://api.nestoria.co.uk/api?country=uk&action=search_listings&place_name=glenavy&encoding=json&listing_type=buy&number_of_results='50'"
 
response = urllib2.urlopen(NESTORIA_API_URL)
results = json.load(response) 
 
Property = namedtuple('Property', [
    "auction_date",  "bathroom_number", "bedroom_number", "car_spaces", 
    "commission", "construction_year", "datasource_name", "guid", "img_height", 
    "img_url", "img_width", "keywords", "latitude", "lister_name", "lister_url",
    "listing_type", "location_accuracy", "longitude", "price", "price_coldrent",
    "price_currency", "price_formatted", "price_high", "price_low", "price_type",
    "property_type", "summary", "thumb_height", "thumb_url", "thumb_width", 
    "title", "updated_in_days", "updated_in_days_formatted",
])
 
def get_properites():
    properties = {}
 
    for result in results['response']['listings']:
        properties[result['guid']] = Property(**result)
 
    return properties
