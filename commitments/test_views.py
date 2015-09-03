from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

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


class TestCommitmentsView(APITestCase):
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
        request = self.factory.get('/profile/commitments/')
        force_authenticate(request, user=self.user)
        response = views.commitments_list(request)
        print (response.data)
        