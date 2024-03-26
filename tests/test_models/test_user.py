#!/usr/bin/python3
from models.user import User
from tests.test_models.test_base_model import TestBaseModel


class TestUser(TestBaseModel):
    '''
    =========================
    User testers
    =========================
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructor testers
        '''
        super().__init__(*args, **kwargs)
        self.test_class = User
        self.test_name = "User"

    def test_email(self):
        '''
        Attribute tester
        '''
        user = self.test_class()
        self.assertIsInstance(user.email, str)

    def test_password(self):
        '''
        Attribute tester
        '''
        user = self.test_class()
        self.assertIsInstance(user.password, str)

    def test_firstName(self):
        '''
        Attribute tester
        '''
        user = self.test_class()
        self.assertIsInstance(user.first_name, str)

    def test_lastName(self):
        '''
        Attribute tester
        '''
        user = self.test_class()
        self.assertIsInstance(user.last_name, str)
