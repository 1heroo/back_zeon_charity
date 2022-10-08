from rest_framework import generics, status, permissions
from .models import MyUser
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    RegUserSerializer,
    MyTokenObtainPairSerializer,
    ResetPasswordSerializer,
    # ForgetPasswordSerializer
)


class APIUserRegistration(generics.GenericAPIView):
    serializer_class = RegUserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = RegUserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Response': 'Created new User'}, status=status.HTTP_201_CREATED)
        return Response('asd', status=status.HTTP_400_BAD_REQUEST)


class ResetPassword(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_password = serializer.data['new_password']
        user = request.user
        user.set_password(new_password)
        user.save()
        return Response('Reset successfully', status=status.HTTP_202_ACCEPTED)


# class ForgetPassword(generics.GenericAPIView):
#     serializer_class = ForgetPasswordSerializer
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exeption=True)


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
