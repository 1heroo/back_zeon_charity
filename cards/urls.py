from django.urls import path, include
from cards import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'cards', views.FundraisingCardViewSet)
router.register(r'volunteering', views.VolunteeringCardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]