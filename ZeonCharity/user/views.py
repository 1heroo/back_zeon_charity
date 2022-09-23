
from django.shortcuts import render
from rest_framework import generics
from .models import MyUser
from rest_framework.response import Response
from .serializers import RegUserSerializer
from django.db.utils import IntegrityError
from django.contrib.auth.hashers import make_password


class APIUserRegistration(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = RegUserSerializer

    def post(self, request):

        data = request.data

        try:
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
        except IntegrityError:
            return Response({'output data': "User '{}' already exists".format(data['username'])})