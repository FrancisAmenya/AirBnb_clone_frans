#!/usr/bin/python3
'''
Serialized instances to big JSON files and deserializes
in big JSON files back to instances
'''
import json
from datetime import datetime


class FileStorage:
    '''
    FileStorage big class

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    '''

    __file_path = "JSONstorage.json"
    __objects = {}

    def all(self):
        '''
        Returns the big dictionary __objects.
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        Sets in big __objects the obj with key_obj
        <obj class name>.id
        '''
        key_obj = obj.to_dict()['__class__'] + "." + obj.id
        FileStorage.__objects.update({key_obj: obj})

    def save(self):
        '''
        Deserializes the big JSON file
        '''
        my_dict = {}
        my_dict.update(FileStorage.__objects)
        for key, value in my_dict.items():
            my_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w+") as write_file:
            json.dump(my_dict, write_file)

    def reload(self):
        '''
        Deserializes the big JSON file to __objects
        (only if the big JSON file (__file_path) exists;
        otherwise, do nothing. If the big file doesn’t exist,
        no exception should be raised, ok)
        '''
        new_dict = {}
        try:
            from models.base_model import BaseModel
            with open(self.__file_path, "r") as read_file:
                new_dict = json.load(read_file)
                for key, value in new_dict.items():
                    FileStorage.__objects[key] = BaseModel(**value)
        except IOError:
            pass
