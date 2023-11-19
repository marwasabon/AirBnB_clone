#!/usr/bin/python3
'''
Test module for amenity class
'''
from models.amenity import Amenity
import unittest


class test_amenity_class(unittest.TestCase):
    '''
    test class for amenity class
    '''
    def setUp(self):
        '''
        Setup class
        '''
        self.new_amenity = Amenity()

    def test_amenity_instance(self):
        '''
        Test the instance of new_amenity
        '''
        self.assertIsInstance(self.new_amenity, Amenity)

    def test_amenity_attribute(self):
        '''
        Test presence of amenity attributes
        '''
        self.assertTrue(hasattr(self.new_amenity, 'name'))
        self.assertEqual(type(self.new_amenity.name), str)
