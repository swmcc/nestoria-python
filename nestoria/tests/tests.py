import unittest

from lib.nestoria import get_all_listings

class TestNestoria(unittest.TestCase):

    def setUp(self):
        default_parameters = {
            'place_name': 'London',
        }

        self.parameters = {'place_name':'London'}

    def testPagination(self):
        parameters = self.parameters
        properties = get_all_listings(parameters)

        parameters['page'] = 2
        second_properties = get_all_listings(parameters)

        self.assertFalse(set(properties) == set(second_properties), 
            'Pagination is returning the same results')

if __name__ == '__main__':
    unittest.main()
