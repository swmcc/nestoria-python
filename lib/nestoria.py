import urllib2
import json

from collections import namedtuple
from urllib import urlencode

NESTORIA_API_URL = 'http://api.nestoria.co.uk/api?'

Property = namedtuple('Property', [
    'auction_date',  'bathroom_number', 'bedroom_number', 'car_spaces',
    'commission', 'construction_year', 'datasource_name', 'guid', 'img_height',
    'img_url', 'img_width', 'keywords', 'latitude', 'lister_name', 'lister_url',
    'listing_type', 'location_accuracy', 'longitude', 'price', 'price_coldrent',
    'price_currency', 'price_formatted', 'price_high', 'price_low', 'price_type',
    'property_type', 'summary', 'thumb_height', 'thumb_url', 'thumb_width',
    'title', 'updated_in_days', 'updated_in_days_formatted',
])

api_elements = [
    'place_name', 'south_west', 'north_east', 'centre_point', 'radius',
    'number_of_results', 'listing_type', 'property_type', 'price_max',' price_min',
    'bedroom_max', 'bedroom_min', 'size_max', 'size_min', 'sort', 'keywords',
    'keywords_exclude', 'action', 'number_of_results', 'country', 'encoding'
]

api_defaults = { 
    'action': 'search_listings',
    'country': 'uk',
    'encoding': 'json',
    'number_of_results': '50',
    'sort': 'newest',
}

def _build_parameters(parameters={}):
    api_parameters = {}
    for element in [x for x in parameters if x in api_elements]:
        # should validate the data passed in not just the element name
        api_parameters[element] = parameters[element]

    for element in api_defaults.keys(): 
        if element not in api_parameters:
            api_parameters[element] = api_defaults[element]

    return urlencode(api_parameters)

def _get_results(parameters={}):
    api_parameters = _build_parameters(parameters)

    response = urllib2.urlopen(NESTORIA_API_URL + api_parameters)
    results = json.load(response)

    return results

def search_listings(parameters={}):
    properties = {}
    parameters['action'] = 'search_listings'

    results = _get_results(parameters)

    if results['response']['application_response_code'].startswith('1'):
        for result in results['response']['listings']:
            properties[result['guid']] = Property(**result)

    return properties

if __name__ == '__main__':
   print search_listings({'place_name':'Glenavy'})
