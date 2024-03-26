#!/usr/bin/python3
"""
inherits from The BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class has its public attributes
    
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """
    place_id = ""
    user_id = ""
    text = ""


def __init__(self, *args, **kwargs):
    """
    The init
    """
    super().__init__(*args, **kwargs)
