from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
from accounts import backends

class TestAuthentication(TestCase):
    def setUp(self):
        self.username = "test_user"
        self.email = "test@email.com"
        self.password = "test_password"
        self.user =  get_user_model().objects.create_user(
                username = self.username,
                email = self.email,
                password = self.password,
            )

class TestBackend(TestAuthentication):
    def setUp(self):
        super(TestBackend, self).setUp()
        self.dummy_backend = backends.EmailOrUsernameAuthBackend()

    def test_lookup_by_username(self):
        result_user = self.dummy_backend._lookup_user(self.username)
        self.assertEqual(result_user.id, self.user.id)

    def test_fail_lookup_by_username(self):
        result_user = self.dummy_backend._lookup_user("")
        self.assertEqual(result_user, None)

    def test_lookup_by_email(self):
        result_user = self.dummy_backend._lookup_user(self.email)
        self.assertEqual(result_user.id, self.user.id)
        
    def test_authenticate_by_username(self):
        result_user = self.dummy_backend.authenticate(self.username, self.password)
        self.assertEqual(result_user.id, self.user.id)

    def test_authenticate_by_email(self):
        result_user = self.dummy_backend.authenticate(self.email, self.password)
        self.assertEqual(result_user.id, self.user.id)

    def test_get_user(self):
        result_user = self.dummy_backend.get_user(self.user.id)
        self.assertEqual(result_user.id, self.user.id)

