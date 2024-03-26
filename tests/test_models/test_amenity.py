#!/usr/bin/python3

from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel


class TestAmenity(TestBaseModel):
    '''
    =========================
    Amenity testers
    =========================
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructor tester
        '''
        super().__init__(*args, **kwargs)
        self.test_class = Amenity
        self.test_name = "Amenity"

    def test_amenity(self):
        '''
        Attribute tester
        '''
        amenity = self.test_class()
        self.assertIsInstance(amenity.name, str)
