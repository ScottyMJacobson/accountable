from rest_framework import serializers

from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    commitmentprofile = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = User
        fields = ('email', 'username', 'date_joined',
            'is_active', 'commitmentprofile')

