#!/usr/bin/python3
'''
Test module for  place class
'''
from models.place import Place
import unittest


class test_place_class(unittest.TestCase):
    '''
    Test fixtures
    '''
    def setUp(self):
        '''
        setup instance
        '''
        self.new_place = Place()

    def test_instance(self):
        '''
        test new_place instance
        '''
        self.assertIsInstance(self.new_place, Place)

    def test_instance_attr(self):
        '''
        test the object attributes
        '''
        self.assertTrue(hasattr(self.new_place, 'city_id'))
        self.assertEqual(type(self.new_place.city_id), str)
        self.assertTrue(hasattr(self.new_place, 'user_id'))
        self.assertEqual(type(self.new_place.user_id), str)
        self.assertTrue(hasattr(self.new_place, 'name'))
        self.assertEqual(type(self.new_place.name), str)
        self.assertTrue(hasattr(self.new_place, 'description'))
        self.assertEqual(type(self.new_place.description), str)
        self.assertTrue(hasattr(self.new_place, 'number_rooms'))
        self.assertEqual(type(self.new_place.number_rooms), int)
        self.assertTrue(hasattr(self.new_place, 'number_bathrooms'))
        self.assertEqual(type(self.new_place.number_bathrooms), int)
        self.assertTrue(hasattr(self.new_place, 'max_guest'))
        self.assertEqual(type(self.new_place.max_guest), int)
        self.assertTrue(hasattr(self.new_place, 'price_by_night'))
        self.assertEqual(type(self.new_place.price_by_night), int)
        self.assertTrue(hasattr(self.new_place, 'longitude'))
        self.assertEqual(type(self.new_place.longitude), float)
        self.assertTrue(hasattr(self.new_place, 'latitude'))
        self.assertEqual(type(self.new_place.latitude), float)
        self.assertTrue(hasattr(self.new_place, 'amenity_ids'))
        self.assertEqual(type(self.new_place.amenity_ids), list)
