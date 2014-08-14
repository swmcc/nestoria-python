import urllib2
import json

from collections import namedtuple
from urllib import urlencode

Property = namedtuple('Property', [
    "auction_date",  "bathroom_number", "bedroom_number", "car_spaces", 
    "commission", "construction_year", "datasource_name", "guid", "img_height", 
    "img_url", "img_width", "keywords", "latitude", "lister_name", "lister_url",
    "listing_type", "location_accuracy", "longitude", "price", "price_coldrent",
    "price_currency", "price_formatted", "price_high", "price_low", "price_type",
    "property_type", "summary", "thumb_height", "thumb_url", "thumb_width", 
    "title", "updated_in_days", "updated_in_days_formatted",
])
 
api_elements = [
    'place_name', 'south_west', 'north_east', 'centre_point', 'radius',
    'number_of_results', 'listing_type', 'property_type', 'price_max',' price_min',
    'bedroom_max', 'bedroom_min', 'size_max', 'size_min', 'sort', 'keywords',
    'keywords_exclude'
]
 
def _build_parameters(parameters={}):
    api_parameters = {}
    for element in [x for x in parameters if x in api_elements]:
        # should validate the data passed in not just the element name
        api_parameters[element] = parameters[element]

    # these aren't really hardcoded so will change this
    harcoded_parameters = {'action':'search_listings', 'number_of_results':'50', 'country':'uk', 'encoding':'json'}

    parameters = dict(api_parameters.items() + harcoded_parameters.items())
    return urlencode(parameters)

def _get_results(parameters={}):
    api_parameters = _build_parameters(parameters)
    
    NESTORIA_API_URL = "http://api.nestoria.co.uk/api?" + api_parameters

    response = urllib2.urlopen(NESTORIA_API_URL)
    results = json.load(response)

    return results

def search_listings(parameters={}):
    
    properties = {}
    results = _get_results(parameters)
    print results
    if results['response']['application_response_code'].startswith('1'):
        for result in results['response']['listings']:
            properties[result['guid']] = Property(**result)

    return properties

if __name__ == '__main__':
    print search_listings({'place_name':'Glenavy'})
