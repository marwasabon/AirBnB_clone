#!/usr/bin/python3
'''
Review class test suite
'''
from models.review import Review
import unittest


class test_review(unittest.TestCase):
    '''
    Test fixture for  review class
    '''
    def setUp(self):
        '''
        setup the class instance
        '''
        self.new_review = Review()

    def test_instance(self):
        '''
        Test object instance
        '''
        self.assertIsInstance(self.new_review, Review)

    def test_instance_attr(self):
        '''
        test the instance attributes
        '''
        self.assertTrue(hasattr(self.new_review, 'place_id'))
        self.assertEqual(type(self.new_review.place_id), str)
        self.assertTrue(hasattr(self.new_review, 'user_id'))
        self.assertEqual(type(self.new_review.user_id), str)
        self.assertTrue(hasattr(self.new_review, 'text'))
        self.assertEqual(type(self.new_review.text), str)
