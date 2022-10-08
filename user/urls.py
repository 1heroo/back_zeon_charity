from django.urls import path
from .views import (
    APIUserRegistration,
    MyTokenObtainPairView,
    ActivationView,
    ResetPassword,
    # ForgetPassword,
)
from rest_framework_simplejwt.views import (\
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # path('api/ forgot-password/', ForgetPassword.as_view(), name='forget'),
    path('api/reset-password/', ResetPassword.as_view(), name='reset'),
    path('api/activation/<str:code>', ActivationView.as_view(), name='activation'),
    path('api/register/', APIUserRegistration.as_view()),
    path('api/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
