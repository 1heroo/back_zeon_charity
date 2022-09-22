from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class MyUser(AbstractUser, PermissionsMixin):
    phone_number = models.IntegerField(default=555)



    def __str__(self) -> str:
        return f'{super().first_name} {super().last_name}'


from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None