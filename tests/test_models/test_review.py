#!/usr/bin/python3
from models.review import Review

from tests.test_models.test_base_model import TestBaseModel


class TestReview(TestBaseModel):
    '''
    =========================
    Review testers
    =========================
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructor testers
        '''
        super().__init__(*args, **kwargs)
        self.test_class = Review
        self.test_name = "Review"

    def test_place_id(self):
        '''
        Attribute tester
        '''
        review = self.test_class()
        self.assertIsInstance(review.place_id, str)

    def test_user_id_review(self):
        '''
        Attribute tester
        '''
        review = self.test_class()
        self.assertIsInstance(review.user_id, str)

    def test_text(self):
        '''
        Attribute tester
        '''
        review = self.test_class()
        self.assertIsInstance(review.text, str)
