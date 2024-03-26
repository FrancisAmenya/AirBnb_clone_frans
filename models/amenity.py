#!/usr/bin/python3
'''
The Amenity class
'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''
    The Amenity class inherits from BaseModel

    Attributes:
        name (str): The name of the amenity.
    '''
    name = ''


def __init__(self, *args, **kwargs):
    """
    init thy self
    """
    super().__init__(*args, **kwargs)
