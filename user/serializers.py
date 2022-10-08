from .models import MyUser
from django.core.mail import send_mail
from rest_framework import serializers
from django.urls import reverse
from django.core.validators import RegexValidator

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# import re


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'phone_number')

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance



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


class UpdatePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(
        max_length=100,
        validators=(RegexValidator(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"),)
    )


# class ForgetPasswordSerializer(serializers.Serializer):
#     email = serializers.CharField(
#         max_length=100,
#         validators=(EmailValidator, )
#     )


# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#
#     def validate_email(self, email):
#         if MyUser.objects.filter(email=email).exists():
#             if MyUser.objects.get(email=email).is_active:
#                 return email
#             raise serializers.ValidationError('Not activated user')
#
#         else:
#             raise serializers.ValidationError('Email Not Found')
#
#
#     def validate(self, attrs):
#         data = super(MyTokenObtainPairSerializer, self).validate(attrs)
#         data['first_name'] = self.user.first_name
#         data['last_name'] = self.user.last_name
#         data['email'] = attrs['email']
#         data['phone_number'] = self.user.phone_number
#         data['password'] = attrs['password']
#         return data




