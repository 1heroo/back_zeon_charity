from django.db import models
from datetime import datetime

from cards.models import FundraisingCard
from user.models import MyUser, Wallet


class Donations(models.Model):

    user_id = models.IntegerField(verbose_name='user', null=True, blank=True)
    card = models.ForeignKey(
        verbose_name='card',
        to=FundraisingCard,
        related_name='donations',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    amount = models.DecimalField(default=.0, decimal_places=2, max_digits=9, blank=False)
    payment_dt = models.DateTimeField(verbose_name='payment_dt', default=datetime.now(), blank=True, null=True)
    payment_success = models.BooleanField(default=False)

    def update_donation_success(self):
        self.payment_success = True

    class Meta:
        verbose_name = 'Donation'
        verbose_name_plural = 'Donations'


class WalletTransactions(models.Model):

    user = models.ForeignKey(
        verbose_name='user',
        to=MyUser,
        related_name='wallet_transactions',
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    amount = models.DecimalField(default=.0, decimal_places=2, max_digits=9, blank=False)
    payment_dt = models.DateTimeField(verbose_name='payment_dt', default=datetime.now(), blank=True, null=True)
    payment_success = models.BooleanField(default=False)

    def update_wallet_transactions_success(self):

        if not self.payment_success:
            self.payment_success = True
            user_wallet = Wallet.objects.get(user=self.user)
            user_wallet.balance += self.amount
            user_wallet.balance_is_active = True
            user_wallet.save()

    class Meta:
        verbose_name = 'Wallet-Transaction'
        verbose_name_plural = 'Wallet-Transactions'
