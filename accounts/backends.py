from django.conf import settings
from django.contrib.auth.models import check_password
from accounts.models import User
from django.core.validators import validate_email
from django.forms import ValidationError

class EmailOrUsernameAuthBackend(object):
    """
    A custom authentication backend. Allows users to log in using their email address or username.
    """

    def _lookup_user(self, username_or_email):
        try:
            validate_email(username_or_email)
                # Looks like an email. Since emails are not case sensitive
                # and many users have a habit of typing them in mixed
                # cases, we will normalize them to lower case. This assumes
                # that the database has done the same thing.
            using_email = True
        except ValidationError:
            using_email = False
        
        try:
            if using_email:
                user = User.objects.get(email=username_or_email.lower())
            else:
                user = User.objects.get(username=username_or_email)
        except User.DoesNotExist:
            return None

        return user

    def authenticate(self, username_or_email=None, password=None):
        """
        Authentication method
        """
        user = self._lookup_user(username_or_email)

        if user:
            if user.check_password(password):
                return user

        return None
        

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
