from rest_framework import generics, status, permissions
from .models import MyUser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    RegUserSerializer,
    ProfileSerializer,
    ResetPasswordSerializer,
    ResetPasswordCompleteSerializer,
    # MyTokenObtainPairSerializer,
)

# password reset libs
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

# from rest_framework_simplejwt.views import TokenObtainPairView


class UserProfileAPIView(generics.GenericAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        return Response({'user-info': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        serializer = self.get_serializer(data=request.data, instance=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Response:': "Successfully updated"}, status=status.HTTP_200_OK)


class UserRegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'New user': request.data}, status=status.HTTP_201_CREATED)


class ActivationAPIView(generics.GenericAPIView):

    def get(self, request, code):
        try:
            user = MyUser.objects.get(code=code)
            user.is_active = True
            user.code = ''
            user.save()
            return Response('Account successfully activated', status=status.HTTP_201_CREATED)
        except MyUser.DoesNotExist:
            return Response('Invalid code', status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordAPIView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': 'something'})


class PasswordTokenVerifyAPIView(generics.GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            pk = smart_str(
                urlsafe_base64_decode(
                    uidb64
                )
            )
            user = MyUser.objects.get(pk=pk)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'Error': 'This token is not valid'}, status=status.HTTP_400_BAD_REQUEST)
            data = {
                'success': True,
                'message': 'Credentials Valid',
                'uidb64': uidb64,
                'token': token
            }
            return Response({'Response': data}, status=status.HTTP_202_ACCEPTED)

        except DjangoUnicodeDecodeError:
            return Response({'Error': 'Invalid uidb64'}, status=status.HTTP_406_NOT_ACCEPTABLE)


class ResetPasswordCompleteAPIView(generics.GenericAPIView):
    serializer_class = ResetPasswordCompleteSerializer

    def patch(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'Response': f'Password successfully changed!'})

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
