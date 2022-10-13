from rest_framework import serializers
from .models import Donations, WalletTransactions


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donations
        fields = "__all__"


class DonationAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donations
        fields = ['card', 'amount']


class WalletTransactionAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletTransactions
        fields = ['amount']


class WalletTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletTransactions
        fields = ['user', 'amount']

