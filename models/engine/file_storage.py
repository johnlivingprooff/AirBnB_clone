#!/usr/bin/python3
"""Defines the FileStorage class"""
from models import base_model
import json


class FileStorage:
    """the FileStorage class that stores dictionary
    representations of objects in a json file
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dict repr of object"""
        return FileStorage.__objects
    
    def new(self, obj):
        """populates the objects dict with new obj
        using obj_class_name.id as the key
        """
        key = obj.to_dict()['__class__'] + '.' + obj.id
        self.all().update({key: obj})

    def save(self):
        """Serialisation:
        saves the dictionary repr of
        an object in a json file"""
        with open(FileStorage.__file_path, 'w') as file:
            temp = FileStorage.__objects
            json.dump(temp, file)
        
    def reload(self):
        """Deserialisation:
        loads a json file to the objects dict
        if the file exisit"""

        with open(FileStorage.__file_path, 'r') as file:
            json.load(FileStorage.__objects, file)
