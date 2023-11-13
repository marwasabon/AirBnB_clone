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


class test_storage_class(unittest.TestCase):
    '''Test suit for FileStorage class'''
    def setUp(self):
        '''Set as instance for every test'''
        self.my_dic = {
            "id": "25",
            "__class__": "model",
            "name": "Okibe",
            "career": "pharmacist"
            }
        self.storage = FileStorage()

    def test_instance_attributes(self):
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
        my_dic = {
                "id": "25",
                "__class__": "model",
                "name": "Okibe",
                "career": "pharmacist"
                }
        self.storage.new(my_dic)
        storage_dict = self.storage._FileStorage__objects
        self.assertEqual(len(storage_dict), 1)
        self.assertIn(my_obj.__class__.__name__ + "." + my_obj.id, storage_dict)

    def test_save_method(self):
        '''Test the save method FileStorage'''
        path = self.storage._FileStorage__file_path
        self.assertFalse(os.path.isfile(path))
        self.storage.new(self.my_dic)
        self.storage.save()
        self.assertTrue(os.path.exists(path))
        self.assertNotEqual(os.path.getsize, 0)
        os.remove(path)

    def test_reload(self):
        '''Test the reload method of FileStorage'''
        path = self.storage._FileStorage__file_path
        self.storage.new(self.my_dic)
        obj = self.storage._FileStorage__objects
        self.storage.save()
        self.storage.reload()
        self.assertIn(my_obj.__class__.__name__ + "." + my_obj.id, storage_dict)
        os.remove(path)
