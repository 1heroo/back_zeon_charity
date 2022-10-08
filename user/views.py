from rest_framework import generics, status, permissions
from .models import MyUser
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

from .serializers import (
    RegUserSerializer,
    UpdatePasswordSerializer,
    ProfileSerializer,
    # ForgetPasswordSerializer,
    # MyTokenObtainPairSerializer,
)
# from rest_framework_simplejwt.views import TokenObtainPairView


class APIUserProfile(generics.GenericAPIView):
    serializer_class = ProfileSerializer
    # permission_classes = (IsAuthenticated, )

    def get(self, request, pk):
        try:
            user = MyUser.objects.get(pk=pk)
            return Response({'user-info': self.get_serializer(user).data}, status=status.HTTP_200_OK)
        except MyUser.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            user = MyUser.objects.get(pk=pk)
            serializer = self.get_serializer(data=request.data, instance=user)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'Response:': "Successfully updated"}, status=status.HTTP_200_OK)

        except MyUser.DoesNotExist:
            return Response({'error': 'User does not exist'})


class APIUserRegistration(generics.GenericAPIView):
    serializer_class = RegUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'New user': request.data}, status=status.HTTP_201_CREATED)
        return Response('Not valid data', status=status.HTTP_400_BAD_REQUEST)


class UpdatePassword(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = UpdatePasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_password = serializer.data['new_password']
        user = request.user
        user.set_password(new_password)
        user.save()
        return Response('Password successfully updated!', status=status.HTTP_202_ACCEPTED)


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


class APIUserAuth(generics.GenericAPIView):
    pass


# class ForgetPassword(generics.GenericAPIView):
#     serializer_class = ForgetPasswordSerializer
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
