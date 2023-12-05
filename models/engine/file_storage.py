#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
from models.base_model import BaseModel
import models

class FileStorage:
    """the FileStorage class that stores dictionary
    representations of objects in a json file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dict repr of object"""
        return self.__objects
    
    def new(self, obj):
        """populates the objects dict with new obj
        using obj_class_name.id as the key
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialisation:
        saves the dictionary repr of
        an object in a json file
        """
        temp_dict = {}
        for key, value in self.__objects.items():
            temp_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as data_file:
            json.dump(temp_dict, data_file)
        
    def reload(self):
        """Deserialisation:
        loads a json file to the objects dict
        if the file exisit"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as data_file:
                new_obj = json.load(data_file)
                for key, value in new_obj.items():
                    temp_obj = eval('{}(**value)'.format(value['__class__']))
                    self.__objects[key] = temp_obj
        except FileNotFoundError:
            pass
