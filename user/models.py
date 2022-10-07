from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string


class MyUser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=False, blank=True)
    code = models.CharField(max_length=10, blank=True)
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
        blank=True, max_length=120,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return f'{super().first_name} {super().last_name}'

    def set_code(self):
        code = get_random_string(10)
        self.code = code
        self.save()
        return code

