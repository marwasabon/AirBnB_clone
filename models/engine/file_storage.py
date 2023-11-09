#!/usr/bin/python3
'''Contains a storage handling class'''
import json
import os


class FileStorage():
    '''
    Serializes instnaces to JSON file and deserialize JSON file to instances
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
        key = obj["__class__"] + obj["id"]
        self.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file (path: __file_path)'''
        with open(self.__file_path, 'w', encoding="utf-8") as fp:
            json.dump(self.__objects, fp, indent=2)

    def reload(self):
        '''Deserializes the JSON file to _objects if __filepath exist'''
        if (os.path.isfile(self.__file_path)):
            with open(self.__file_path, 'r', encoding="utf-8") as fp:
                self.__objects = json.load(fp)

    def __str__(self):
        '''return string representation of __objects'''
        return str(self.__objects)
