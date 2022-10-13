from django.urls import path
from payments.views import DonationView, DonationSuccessView, FailureView, \
    WalletTransactionsView, SuccessBalanceUpdateView

urlpatterns = [
    path('donation/', DonationView.as_view()),
    path('donation/success/', DonationSuccessView.as_view()),

    path('fill-up-a-balance/', WalletTransactionsView.as_view()),
    path('balance/success/', SuccessBalanceUpdateView.as_view()),

    path('transaction/failure/', FailureView.as_view()),

]
