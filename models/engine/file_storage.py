#!/usr/bin/python3
'''Contains a storage handling class'''
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage():
    '''Serializes instnaces to JSON file and deserialize JSON file to instances


    Attr:
        __file_path(str): string to teh JSON file
        __objects(dict): dictionary to store all objects
    '''
    __file_path = 'file.json'
    __objects = dict()

    class_dict = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def all(self, cls=None):
        '''returns dictionary __objects'''
        if cls:
            objects = storage.all(cls)
            for key in objects:
                print(objects[key])
        else:
            objects = storage.all()
            for key in objects:
                print(objects[key])
        
    def alls(self):
        '''returns dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj classname.id>

        Args:
            obj: dictionary representation of an object
        '''
        obj_dict = obj.to_dict()
        key = obj_dict["__class__"] + "." + obj_dict["id"]
        self.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file (path: __file_path)'''
        new_dict = dict()
        with open(self.__file_path, 'w', encoding="utf-8") as fp:
            for key, val in self.__objects.items():
                new_dict[key] = val.to_dict()
            json.dump(new_dict, fp, indent=2)

    def reload(self):
        '''Deserializes the JSON file to _objects if __filepath exist'''
        if (os.path.isfile(self.__file_path)):
            with open(self.__file_path, 'r', encoding="utf-8") as fp:
                dic_obj = json.load(fp)
                for key, dic in dic_obj.items():
                    class_name = dic['__class__']
                    del dic['__class__']
                    if class_name in self.class_dict:
                        cls = self.class_dict[class_name]
                        obj = cls(**dic)
                        self.__objects[key] = obj

