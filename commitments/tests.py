from django.test import TestCase
from django.contrib.auth import get_user_model
from commitments.models import *


class DummyUserTestCase(TestCase):
    def setUp(self):
        self.username = "test_user"
        self.email = "test@email.com"
        self.password = "test_password"
        self.user =  get_user_model().objects.create_user(
                username = self.username,
                email = self.email,
                password = self.password,
            )

class CommitmentProfileTestCase(DummyUserTestCase):
    def test_user_with_profile(self):
        """make sure that the commitmentprofile gets automatically generated"""
        my_commitment_profile = self.user.commitmentprofile
        if my_commitment_profile is None:
            self.fail("Commitment profile doesn't exist")

    def test_add_commitment_to_user(self):
        dummy_commitment_name = 'brush_teeth'
        dummy_commitment_description = 'brush your teeth every night'
        my_commitment_profile = self.user.commitmentprofile
        my_commitment_profile.register_commitment(dummy_commitment_name, 
            dummy_commitment_description)
        all_commitments = my_commitment_profile.get_active_commitments()
        self.assertEqual(all_commitments[0].name, dummy_commitment_name)
        self.assertEqual(all_commitments[0].description, dummy_commitment_description)

