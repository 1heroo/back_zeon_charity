import requests
import xmltodict
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotAcceptable
from rest_framework.permissions import IsAuthenticated


from .models import Donations, WalletTransactions
from user.models import MyUser, Wallet
from .confirmations import MERCHANT_ID, get_paybox_params
from .confirmations import get_sig, get_salt, is_real_signature
from .serializers import DonationSerializer, DonationAmountSerializer, WalletTransactionSerializer, \
    WalletTransactionAmountSerializer


class DonationView(generics.CreateAPIView):
    queryset = Donations.objects.all()
    serializer_class = DonationAmountSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = MyUser.objects.get(id=1)
        # user = request.user
        data['user'] = user
        user_wallet = Wallet.objects.get(user=2)
        if user_wallet.balance_is_active:
            if float(user_wallet.balance) >= float(data['amount']):
                user_wallet.balance = float(user_wallet.balance) - float(data['amount'])
                user_wallet.save()

                second_ser = DonationSerializer(data=data)
                second_ser.is_valid(raise_exception=True)
                second_ser.save()
                return Response({"pg_transaction_status": 'OK'})

        second_ser = DonationSerializer(data=data)
        second_ser.is_valid(raise_exception=True)
        payment = second_ser.save()

        params = get_paybox_params(payment)
        params['pg_sig'] = get_sig(params, method='init_payment.php')
        r = requests.post('https://api.paybox.money/init_payment.php', params=params)
        payload = xmltodict.parse(r.content).get('response', {})
        if payload.get('pg_status') != 'ok':
            raise NotAcceptable
        return Response({"url": payload.get('pg_redirect_url')})


class DonationSuccessView(APIView):

    def get(self, request):

        if is_real_signature(request):
            order_id = request.GET.get('pg_order_id')
            payment = Donations.objects.get(id=order_id)
            payment.payment_success = True
            payment.save()

        return Response({"pg_transaction_status": 'OK'})


class FailureView(APIView):

    def get(self, request):

        if is_real_signature(request):

            payment_id = request.GET.get('pg_payment_id')
            order_id = request.GET.get('pg_order_id')

            params = dict(
                pg_merchant_id=MERCHANT_ID,
                pg_payment=payment_id,
                pg_order_id=order_id,
                pg_salt=get_salt(),
            )
            params['pg_sig'] = get_sig(params, method='get_status2.php')
            r = requests.post('https://api.paybox.money/get_status2.php', params=params)
            payload = xmltodict.parse(r.content).get('response', {})
            return Response({
                         "pg_transaction_status": payload.get('pg_transaction_status'),
                         "pg_failure_code": payload.get('pg_failure_code'),
                         "pg_failure_description": payload.get('pg_failure_description'),
                         })


class WalletTransactionsView(generics.CreateAPIView):
    queryset = WalletTransactions.objects.all()
    serializer_class = WalletTransactionAmountSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        data['user'] = request.user.id
        second_ser = WalletTransactionSerializer(data=data)
        second_ser.is_valid(raise_exception=True)
        payment = second_ser.save()

        params = get_paybox_params(payment, balance=True)

        params['pg_sig'] = get_sig(params, method='init_payment.php')
        r = requests.post('https://api.paybox.money/init_payment.php', params=params)
        payload = xmltodict.parse(r.content).get('response', {})
        if payload.get('pg_status') != 'ok':
            raise NotAcceptable
        return Response({"url": payload.get('pg_redirect_url')})


class SuccessBalanceUpdateView(APIView):

    def get(self, request):

        if is_real_signature(request):
            order_id = request.GET.get('pg_order_id')
            payment = WalletTransactions.objects.get(id=order_id)
            payment.update_wallet_transactions_success()
            payment.save()

        return Response({"pg_transaction_status": 'OK'})
