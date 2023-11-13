#!/usr/bin/python
'''
Test cases:
    * Test for existence of all public attributes and their type ////done
    * Test object are instance of class ///done
    * Test all methods
'''
import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class test_storage_class(unittest.TestCase):
    '''Test suit for FileStorage class'''
    def setUp(self):
        '''Set as instance for every test'''
        self.my_dic = BaseModel()
        self.storage = FileStorage()

    def test_instance_attributes(self):
        '''
        Test the attribute type and existence
        '''
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertEqual(type(self.storage._FileStorage__objects), dict)
        self.assertEqual(type(self.storage._FileStorage__file_path), str)
        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(self.storage, '_FileStorage__objects'))

    def test_class_instance(self):
        '''Test if object are instances of FileStorage'''
        self.assertIsInstance(self.storage, FileStorage)

    def test_new_method(self):
        '''Test the new method'''
        self.storage.new(self.my_dic)
        storage_dict = self.storage._FileStorage__objects
        self.assertTrue(len(storage_dict) > 0)
        self.assertEqual(type(storage_dict), dict)

    def test_save_method(self):
        '''Test the save method FileStorage'''
        path = self.storage._FileStorage__file_path
        if os.path.isfile(path):
            os.remove(path)
        self.assertFalse(os.path.isfile(path))
        self.storage.new(self.my_dic)
        self.storage.save()
        self.assertTrue(os.path.exists(path))
        self.assertNotEqual(os.path.getsize, 0)

    def test_reload(self):
        '''Test the reload method of FileStorage'''
        path = self.storage._FileStorage__file_path
        self.storage.new(self.my_dic)
        obj = self.storage._FileStorage__objects
        self.storage.save()
        self.storage.reload()
        self.assertEqual(obj, self.storage._FileStorage__objects)
