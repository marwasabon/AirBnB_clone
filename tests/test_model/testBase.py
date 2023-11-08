#!/usr/bin/python3

from models.base_model import BaseModel
import unittest

# Testing the BaseModel class

class TestBaseModel(unittest.TestCase):
    
    def test_init(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_str(self):
        base_model = BaseModel()
        self.assertEqual(str(base_model), "[BaseModel] ({}) {}".format(base_model.id, base_model.__dict__))


    def test_save(self):
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(initial_updated_at, base_model.updated_at)
    
    def data_test(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        print(my_model)
        my_model.save()
        print(my_model)
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
        
    def test_to_dict(self):
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], base_model.updated_at.isoformat())




if __name__ == "__main__":
    unittest.main()
