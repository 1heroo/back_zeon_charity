from rest_framework import generics, status
from .models import MyUser
from rest_framework.response import Response
from .serializers import RegUserSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class APIUserRegistration(generics.GenericAPIView):
    serializer_class = RegUserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = RegUserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Response': 'Created new User'}, status=status.HTTP_201_CREATED)
        return Response('asd', status=status.HTTP_400_BAD_REQUEST)


class ActivationView(generics.GenericAPIView):
    def get(self, request, code):
        try:
            user = MyUser.objects.get(code=code)
            user.is_active = True
            user.code = ''
            user.save()
            return Response('Account successfully activated', status=status.HTTP_201_CREATED)
        except MyUser.DoesNotExist:
            return Response('Invalid code', status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
