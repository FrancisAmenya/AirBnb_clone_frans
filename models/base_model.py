#!/usr/bin/python3

'''
The class BaseModel that defines all common attributes/methods
for other classes
'''
from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''
    The BaseModel class of the HBnB 
    '''

    def __init__(self, *args, **kwargs):
        '''
        The Constructor method
        '''
        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.save()
            storage.new(self)
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def save(self):
        '''
        The Update public instance with current datetime
        '''
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        '''
        The String reprsentation
        '''
        return '[{}] ({}) {}'.format(
            type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        '''
        The Dictionary containing all pairs of __class__ 
        representing the class name 
        keys/values of __dict__
        '''
        my_cmd_dict = dict(self.__dict__)
        my_cmd_dict['created_at'] = self.created_at.isoformat()
        my_cmd_dict['updated_at'] = self.updated_at.isoformat()
        my_cmd_dict['__class__'] = type(self).__name__
        return my_cmd_dict
