#!/usr/bin/python3
'''
Test suite Model for user class
'''
import unittest
from models.user import User


class Test_user_class(unittest.TestCase):
    '''
    Test suite
    '''
    def setUp(self):
        '''
        setup test objects
        '''
        self.new_user = User()

    def test_instance(self):
        '''
        Test if new_user is an instance of User
        '''
        self.assertIsInstance(self.new_user, User)

    def test_class_attributes(self):
        '''
        Test class attributes
        '''
        self.assertTrue(hasattr(type(self.new_user), "email"))
        self.assertTrue(hasattr(type(self.new_user), "password"))
        self.assertTrue(hasattr(type(self.new_user), "first_name"))
        self.assertTrue(hasattr(type(self.new_user), "last_name"))

    def test_class_instance(self):
        '''
        Test obj is an instance of user class
        '''
        self.assertIsInstance(self.new_user, User)

    def test_classattr_type(self):
        '''
        Test the class attribute type
        '''
        self.assertEqual(type(self.new_user.email), str)
        self.assertEqual(type(self.new_user.password), str)
        self.assertEqual(type(self.new_user.first_name), str)
        self.assertEqual(type(self.new_user.last_name), str)
