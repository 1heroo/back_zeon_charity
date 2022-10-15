from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string


class MyUser(AbstractUser, PermissionsMixin):

    username = models.CharField(max_length=50, unique=False, blank=True)
    code = models.CharField(max_length=10, blank=True)
    phone_number = models.IntegerField(
        _('phone number'),
        default=555,
        blank=True
    )
    email = models.EmailField(
        _("email address"),
        unique=True
    )
    password = models.CharField(
        _("password"),
        blank=True, max_length=120,
    )

    # balance = models.DecimalField(default=.0, decimal_places=2, max_digits=9, blank=False)
    # balance_is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return f'{super().first_name} {super().last_name}'

    def set_code(self):
        code = get_random_string(10)
        self.code = code
        self.save()
        return code


def init_wallet(sender, instance, *args, **kwargs):
    if not Wallet.objects.filter(user=instance):
        wallet_obj = Wallet(
            user=instance,
        )
        wallet_obj.save()


post_save.connect(init_wallet, sender=MyUser)


class Wallet(models.Model):

    user = models.ForeignKey(
        verbose_name='user',
        to=MyUser,
        # to='user.models.MyUser',
        related_name='wallet',
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    balance = models.DecimalField(default=.0, decimal_places=2, max_digits=9, blank=False)
    balance_is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'



