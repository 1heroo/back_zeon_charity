from django.urls import path
from .views import (
    APIUserRegistration,
    MyTokenObtainPairView,
    ActivationView
)
from rest_framework_simplejwt.views import (\
    TokenRefreshView,
    TokenVerifyView,

)

urlpatterns = [
    path('activation/<str:code>', ActivationView.as_view(), name='activation'),
    path('api/register/', APIUserRegistration.as_view()),
    path('api/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
