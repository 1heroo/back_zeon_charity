from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
# Create your models here.


class MyUser(AbstractUser, PermissionsMixin):
    phone_number = models.IntegerField(default=555)

    def __str__(self) -> str:
        return f'{super().first_name} {super().last_name}'
    