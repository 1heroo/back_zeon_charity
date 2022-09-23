from django.shortcuts import render
from rest_framework import generics
from .models import MyUser
from rest_framework.response import Response
from .serializers import RegUserSerializer, LoginSerializer
from django.db.utils import IntegrityError
from django.contrib.auth.hashers import make_password
from django.forms.models import model_to_dict


class APIUserRegistration(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = RegUserSerializer

    def post(self, request):
        data = request.data

        if MyUser.objects.filter(email=data['email']):
            return Response({'output data': "User '{}' already exists".format(data['email'])})

        new_user = MyUser.objects.create(
                username=data['username'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                phone_number=data['phone_number'],
                password=make_password(data['password']),
                email=data['email']
            )
        new_user.save()
        return Response({"output data': 'User '{}' successfully registered!".format(data['username'])})
            


class APIUserLogin(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = LoginSerializer

    def post(self, request):

        data = request.data
        user = MyUser.objects.filter(email=data['email'])[0]
        if user:
            data_d = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'phone_number': user.phone_number           }
            return Response({'info': data_d})
        else:
            return Response({'info': 'User not found'})