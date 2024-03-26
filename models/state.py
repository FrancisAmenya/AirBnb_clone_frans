#!/usr/bin/python3
'''
The State class
'''
from models.base_model import BaseModel


class State(BaseModel):
    '''
    The State class inherits from BaseModel
    
    Attributes:
        name (str): The name of the state.
    '''
    name = ''


def __init__(self, *args, **kwargs):
    """
    The init
    """
    super().__init__(*args, **kwargs)
