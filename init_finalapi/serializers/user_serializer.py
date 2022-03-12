from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """
    class Meta:
        model = User
        fields = ('username', 
                  'email',
                  'password',
                  'lastname',
                  'firstname',
                )