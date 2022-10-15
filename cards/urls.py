from django.urls import path, include
from cards import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
# router.register(r'fundraising', views.FundraisingCardViewSet)
router.register(r'volunteering', views.VolunteeringCardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/create-fundrising/', views.FundraisingCardAPIView.as_view()),
    path('api/help-apply/', views.CardApply.as_view(), name='help-apply'),
    path('api/search/', views.SearchView.as_view(), name='search'),

]
