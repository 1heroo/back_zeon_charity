from hashlib import blake2b
from .models import MyUser
from django.core.mail import send_mail
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.urls import reverse
from django.core.validators import RegexValidator, EmailValidator
import re


class RegUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    phone_number = serializers.IntegerField()

    def validate_email(self, email):
        if MyUser.objects.filter(email=email).exists():
            raise serializers.ValidationError('email already exists')
        return email

    def create(self, validated_data):
        host = 'http://127.0.0.1:8000/'
        password = validated_data.pop('password')
        user = MyUser(**validated_data)
        user.set_password(password)
        user.set_code()
        user.is_active = False
        send_mail(
            subject='Activation',
            message=f'{host}{reverse("activation", kwargs={"code": user.code})}',
            from_email='iswearican.a@gmail.com',
            recipient_list=[user.email],
            fail_silently=False
        )
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate_email(self, email):
        if MyUser.objects.filter(email=email).exists():

            if MyUser.objects.get(email=email).is_active:
                return email
            raise serializers.ValidationError('Not activated user')

        else:
            raise serializers.ValidationError('Email Not Found')


    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        data['email'] = attrs['email']
        data['phone_number'] = self.user.phone_number
        data['password'] = attrs['password']
        return data


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(
        max_length=100,
        validators=(RegexValidator(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"),)
    )


# class ForgetPasswordSerializer(serializers.Serializer):
#     email = serializers.CharField(
#         max_length=100,
#         validators=(EmailValidator, )
#     )



