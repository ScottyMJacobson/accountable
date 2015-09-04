from django.test import TestCase
from django.contrib.auth import get_user_model

from accounts.serializers import UserSerializer

from django.utils import timezone

class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.username = "test_user"
        self.email = "test@email.com"
        self.password = "test_password"
        self.user =  get_user_model().objects.create_user(
                username = self.username,
                email = self.email,
                password = self.password,
            )

    def test_user_serializer(self):
        self.serializer = UserSerializer(self.user)
        self.assertEqual(self.serializer.data['username'], self.username)

