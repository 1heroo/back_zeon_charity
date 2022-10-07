from rest_framework import generics
from .models import MyUser
from rest_framework.response import Response
from .serializers import RegUserSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class APIUserRegistration(generics.GenericAPIView):
    serializer_class = RegUserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        if MyUser.objects.filter(email=data['email']):
            return Response({'Response': "User '{}' already exists".format(data['email'])})

        csrf = data['csrfmiddlewaretoken']
        new_user = MyUser(
                first_name=data['first_name'],
                last_name=data['last_name'],
                phone_number=data['phone_number'],
                email=data['email']
            )
        new_user.set_password(data['password'])
        new_user.save()
        return Response({"Response': 'User '{}' successfully registered!".format(data['first_name'])})


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer