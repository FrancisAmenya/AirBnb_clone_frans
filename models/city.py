#!/usr/bin/python3
'''
The City class
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    The State class inherits from BaseModel

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    '''
    state_id = ''
    name = ''


def __init__(self, *args, **kwargs):
    """
    The init
    """
    super().__init__(*args, **kwargs)
