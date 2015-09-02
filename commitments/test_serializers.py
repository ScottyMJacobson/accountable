from django.test import TestCase
from django.contrib.auth import get_user_model

from commitments.serializers import CommitmentSerializer


class CommitmentSerializerTestCase(TestCase):
    def setUp(self):
        self.username = "test_user"
        self.email = "test@email.com"
        self.password = "test_password"
        self.user =  get_user_model().objects.create_user(
                username = self.username,
                email = self.email,
                password = self.password,
            )
        self.dummy_commitment_name = 'wash face'
        self.dummy_commitment_description = 'wash your face every night'
        my_commitment_profile = self.user.accountableuser
        my_commitment_profile.register_commitment(self.dummy_commitment_name, 
            self.dummy_commitment_description)
        self.dummy_commitment = self.user.accountableuser.get_active_commitments()[0]

    def test_commitment_serializer(self):
        self.serializer = CommitmentSerializer(self.dummy_commitment)
        self.assertEqual(self.serializer.data['name'], self.dummy_commitment_name)
        self.assertEqual(self.serializer.data['owner'], self.user.id)

