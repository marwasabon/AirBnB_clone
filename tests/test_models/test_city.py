#!/usr/bin/python3
'''
Test suit for city class
'''
import unittest
from models.city import City


class test_city_class(unittest.TestCase):
    '''
    Test class  for  city class
    '''

    def setUp(self):
        '''
        setup an instance of city
        '''
        self.new_city = City()

    def test_instance(self):
        '''
        Test the instance of the city class
        '''
        self.assertIsInstance(self.new_city, City)

    def test_instance_attr(self):
        '''
        Test the instance atributes
        '''
        self.assertEqual(type(self.new_city.state_id), str)
        self.assertEqual(type(self.new_city.name), str)
        self.assertTrue(hasattr(self.new_city, "state_id"))
        self.assertTrue(hasattr(self.new_city, "name"))
        self.assertEqual(self.new_city.state_id, '')
        self.assertEqual(self.new_city.name, '')
