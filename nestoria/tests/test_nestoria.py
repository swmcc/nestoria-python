import vcr
import unittest

from nestoria import search_listings

class TestNestoria(unittest.TestCase):

    def setUp(self):
        default_parameters = {
            'place_name': 'London',
        }

        self.parameters = {'place_name':'London'}

    @vcr.use_cassette('tests/fixtures/vcr_cassettes/london_search.yaml')
    def test_pagination(self):
        parameters = self.parameters
        properties = search_listings(parameters)

        parameters['page'] = 2
        second_properties = search_listings(parameters)

        self.assertFalse(set(properties) == set(second_properties),
            'Pagination is returning the same results')


if __name__ == '__main__':
    unittest.main()
