from django.urls import path
from .views import (
    APIUserRegistration,
    # MyTokenObtainPairView,
    ActivationView,
    UpdatePassword,
    APIUserAuth,
    APIUserProfile,
    # ForgetPassword,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenObtainPairView
)

urlpatterns = [
    # path('api/ forgot-password/', ForgetPassword.as_view(), name='forget'),

    # user-related endpoints
    path('api/register/', APIUserRegistration.as_view(), name='register'),
    path('api/authentication', APIUserAuth.as_view(), name='auth'),
    path('api/profile/<int:pk>/', APIUserProfile.as_view(), name='profile'),
    path('api/update-password/', UpdatePassword.as_view(), name='reset'),

    # activation endpoints
    path('api/activation/<str:code>', ActivationView.as_view(), name='activation'),

    # token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
