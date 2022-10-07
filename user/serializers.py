
from hashlib import blake2b
from .models import MyUser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'password', 'email', 'phone_number')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        data['email'] = attrs['email']
        data['phone_number'] = self.user.phone_number
        data['password'] = attrs['password']
        return data