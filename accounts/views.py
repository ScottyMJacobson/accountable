from django.contrib.auth import get_user_model
from accounts.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from accounts.permissions import IsStaffOrTargetUser

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = get_user_model()
    queryset = get_user_model().objects.all()

    def get_permissions(self):
        # Allow anyone to create via POST, only allow views
        # to the user who's looking
        return(AllowAny() if self.request.method == 'POST'
               else IsStaffOrTargetUser()),


