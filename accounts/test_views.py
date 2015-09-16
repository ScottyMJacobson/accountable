from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from rest_framework import status

from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse

from accounts import views

class TestPostUser(APITestCase):
    def test_post_user(self):
        user_dict = {'username': "test_user",
                    'email': "test@email.com",
                    'password': "test_password"}
        url = reverse('accounts:account-list')
        response = self.client.post(url, user_dict, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestGetUser(APITestCase):
    def setUp(self):
        self.username = "test_user"
        self.email = "test@email.com"
        self.password = "test_password"
        self.user =  get_user_model().objects.create_user(
                username = self.username,
                email = self.email,
                password = self.password,
            )

    def test_fail_list_users(self):
        # this should fail because the user isn't a superuser 
        self.client.force_authenticate(user=self.user)
        url = reverse('accounts:account-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_user(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('accounts:account-detail', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
