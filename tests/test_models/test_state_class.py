#!/usr/bin/python3
'''
Test modeule for state class
'''
from models.state import State
import unittest


class test_state_class(unittest.TestCase):
    '''
    test class for state class
    '''
    def setUp(self):
        '''
        Setup class
        '''
        self.new_state = State()

    def test_state_instance(self):
        '''
        Test the instance of new_state
        '''
        self.assertIsInstance(self.new_state, State)

    def test_state_attribute(self):
        '''
        Test presence of state attributes
        '''
        self.assertTrue(hasattr(self.new_state, 'name'))
        self.assertEqual(type(self.new_state) == str)
