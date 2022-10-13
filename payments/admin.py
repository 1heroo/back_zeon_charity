from django.contrib import admin
from .models import Donations, WalletTransactions
from user.models import Wallet


admin.site.register(Donations)
admin.site.register(WalletTransactions)
admin.site.register(Wallet)

