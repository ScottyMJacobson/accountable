from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from rest_framework import status

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from commitments import views


class TestCommitmentProfileView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.username = "test_user"
        self.email = "test@email.com"
        self.password = "test_password"
        self.user =  get_user_model().objects.create_user(
                username = self.username,
                email = self.email,
                password = self.password,
            )

    def test_commitment_profile_view(self):
        # Make an authenticated request to the view...
        request = self.factory.get('/profile/')
        force_authenticate(request, user=self.user)
        response = views.commitment_profile(request)
        self.assertEqual(response.data['user'], self.user.id)


class TestGetCommitmentsView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.username = "test_user"
        self.email = "test@email.com"
        self.password = "test_password"
        self.user =  get_user_model().objects.create_user(
                username = self.username,
                email = self.email,
                password = self.password,
            )

    def test_get_commitments_view(self):
        self.dummy_commitment_name = 'wash face'
        self.dummy_commitment_description = 'wash your face every night'
        my_commitment_profile = self.user.commitmentprofile
        commitment = my_commitment_profile.register_commitment(self.dummy_commitment_name, 
            self.dummy_commitment_description)
        request = self.factory.get('/profile/commitments/')
        force_authenticate(request, user=self.user)
        response = views.commitments_list(request)
        self.assertEqual(response.data[0]['id'], commitment.id)


class TestPostCommitmentsView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.username = "test_user"
        self.email = "test@email.com"
        self.password = "test_password"
        self.user =  get_user_model().objects.create_user(
                username = self.username,
                email = self.email,
                password = self.password,
            )

    def test_post_commitments_view(self):
        commitment_dict = {'name': 'test commit', 'description':'you know what it is'}
        request = self.factory.post('/profile/commitments/', commitment_dict)
        force_authenticate(request, user=self.user)
        response = views.commitments_list(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], commitment_dict['name'])


