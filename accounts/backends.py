from django.conf import settings
from django.contrib.auth.models import check_password
from accounts.models import User

class EmailOrUsernameAuthBackend(object):
    """
    A custom authentication backend. Allows users to log in using their email address or username.
    """

    def authenticate(self, username_or_email=None, password=None):
        """
        Authentication method
        """
        try:
            # maybe they gave us an email!
            user = User.objects.get(email=username_or_email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            # okay maybe they gave us a username!
            try:
                user = User.objects.get(username=username_or_email)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
