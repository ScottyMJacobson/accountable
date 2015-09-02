from django.test import TestCase, Client
from django.conf import settings
from django.contrib.auth import get_user_model
from accounts import backends


class TestLogin(TestCase):
    def setUp(self):
        self.username = "test_user0"
        self.email = "test0@email.com"
        self.password = "test_password0"
        self.user =  get_user_model().objects.create_user(
                username = self.username,
                email = self.email,
                password = self.password,
            )
        self.c = Client()

    def test_username_login(self):
        login_result = self.c.login(username=self.username, password=self.password)
        self.assertTrue(login_result)

    def test_email_login(self):
        login_result = self.c.login(username=self.email, password=self.password)
        self.assertTrue(login_result)

    def test_username_fail(self):
        login_result = self.c.login(username="", password=self.password)
        self.assertFalse(login_result)

    def test_password_fail(self):
        login_result = self.c.login(username=self.username, password="")
        self.assertFalse(login_result)


class TestBackend(TestCase):
    def setUp(self):
        self.username = "test_user"
        self.email = "test@email.com"
        self.password = "test_password"
        self.user =  get_user_model().objects.create_user(
                username = self.username,
                email = self.email,
                password = self.password,
            )
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

