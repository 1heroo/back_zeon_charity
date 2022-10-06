from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# from django.conf import settings


class MyUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=False)
    phone_number = models.IntegerField(
        _('phone number'),
        default=555
    )
    email = models.EmailField(
        _("email address"),
        unique=True
    )
    password = models.CharField(
        _("password"),
        blank=True,max_length=120,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return f'{super().first_name} {super().last_name}'
