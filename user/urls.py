from django.urls import path
from .views import (
    UserRegistrationAPIView,
    ActivationAPIView,
    UserProfileAPIView,
    ResetPasswordAPIView,
    PasswordTokenVerifyAPIView,
    ResetPasswordCompleteAPIView,
)

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenObtainPairView
)

urlpatterns = [

    # user-related endpoints
    path('api/register/', UserRegistrationAPIView.as_view(), name='register'),
    path('api/profile/', UserProfileAPIView.as_view(), name='profile'),

    # reset user's password
    path('api/reset-password-complete/', ResetPasswordCompleteAPIView.as_view(), name='reset-password-complete'),
    path('api/reset-password/', ResetPasswordAPIView.as_view(), name='reset-password'),
    path('api/reset-token-verify/<uidb64>/<token>/', PasswordTokenVerifyAPIView.as_view(), name='reset-token-verify'),

    # activation endpoints
    path('api/activation/<str:code>', ActivationAPIView.as_view(), name='activation'),

    # jwt token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
