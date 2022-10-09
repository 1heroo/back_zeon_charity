import re

from rest_framework.exceptions import AuthenticationFailed

from .models import MyUser
from django.core.mail import send_mail
from django.urls import reverse
from django.core.validators import EmailValidator, RegexValidator
from django.contrib.sites.shortcuts import get_current_site
from decouple import config

# drf libs
from rest_framework import serializers


# password reset libs
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('first_name', 'last_name', 'phone_number', 'password')

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        password = validated_data.get('password', False)

        if password:
            password_validation = re.search(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password)
            if password_validation is None:
                raise serializers.ValidationError('Invalid password')

            send_mail(
                subject='Password have been successfully changed!',
                message=f'Dear {instance.first_name} {instance.last_name}, your password have been changed',
                from_email='iswearican.a@gmail.com',
                recipient_list=[instance.email],
                fail_silently=False
            )

            instance.set_password(password)

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
        host = config("HOST")
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


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=(EmailValidator, )
    )

    def validate(self, attrs):
        email = attrs.get('email', None)
        if MyUser.objects.filter(email=email).exists():
            user = MyUser.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)

            # sending email
            host = config("HOST")
            body = reverse('reset-token-verify', kwargs={
                'uidb64': uidb64,
                'token': token
            })

            activation_link = '{host}{body}'.format(host=host, body=body)
            email_text = f'Dear, {user.first_name}, please click link below to reset your password \n {activation_link}'

            send_mail(
                subject='Password Reset Confirmation',
                message=email_text,
                from_email='iswearican.a@gmail.com',
                recipient_list=[email],
                fail_silently=False
            )
            return attrs
        raise serializers.ValidationError('Email Not Found!')


class ResetPasswordCompleteSerializer(serializers.Serializer):
    password = serializers.CharField(
        validators=(RegexValidator(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"), ),
        write_only=True
    )
    uidb64 = serializers.CharField(min_length=1, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)

    def validate(self, attrs):
        try:
            new_password = attrs.get('password')
            uidb64 = attrs.get('uidb64')
            token = attrs.get('token')

            pk = force_str(
                urlsafe_base64_decode(uidb64)
            )
            user = MyUser.objects.get(pk=pk)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('asd')
            user.set_password(new_password)
            user.save()
            return attrs
        except AuthenticationFailed:
            raise serializers.ValidationError('Invalid token or uidb64')



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