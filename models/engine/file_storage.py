#!/usr/bin/python3
"""Defines the FileStorage class"""
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
        key = f"{obj.to_dict()['__class__']}.{obj.id}"
        self.all().update({key: obj})

    def save(self):
        """Serialisation:
        saves the dictionary repr of
        an object in a json file"""
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as data_file:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, value in temp.items():
                if hasattr(value, 'to_dict'):
                    temp[key] = value.to_dict()
            json.dump(temp, data_file)
        
    def reload(self):
        """Deserialisation:
        loads a json file to the objects dict
        if the file exisit"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as data_file:
                temp = json.load(data_file)
                for key, value in temp.items():
                    self.all()[key] = value
        except FileNotFoundError:
            pass
