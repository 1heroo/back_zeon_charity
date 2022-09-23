from hashlib import blake2b
from .models import MyUser
from rest_framework import serializers


class RegUserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)
    email = serializers.EmailField()
    phone_number = serializers.IntegerField()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)