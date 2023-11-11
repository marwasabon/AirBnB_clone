#!/usr/bin/python3
'''Contains a storage handling class'''
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    '''Serializes instnaces to JSON file and deserialize JSON file to instances


    Attr:
        __file_path(str): string to teh JSON file
        __objects(dict): dictionary to store all objects
    '''
    __file_path = 'file.json'
    __objects = dict()

    def all(self):
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
        dum_dic = dict()
        with open(self.__file_path, 'w', encoding="utf-8") as fp:
            for key, val in self.__objects.items():
                if type(val) != dict:
                    self.__objects[key] = val.to_dict()
            json.dump(self.__objects, fp, indent=2)

    def reload(self):
        '''Deserializes the JSON file to _objects if __filepath exist'''
        if (os.path.isfile(self.__file_path)):
            with open(self.__file_path, 'r', encoding="utf-8") as fp:
                dic_obj = json.load(fp)
                for key, dic in dic_obj.items():
                    class_name = dic['__class__']
                    del dic['__class__']
                    if class_name == 'BaseModel':
                        new_instance = BaseModel(**dic)
                    elif class_name == 'User':
                        new_instance = User(**dic)
                    self.__objects[key] = new_instance
