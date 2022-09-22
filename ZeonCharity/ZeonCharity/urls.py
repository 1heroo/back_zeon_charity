"""ZeonCharity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user.views import *
from .yasg import urlpatterns as swagger
from cards import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'cards', views.CardViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-reg/', APIUserRegistration.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('card/<int:id>',
        views.CardViewSet.as_view({'get': 'list'})
    ),
    path('fund/<int:id>',
        views.FundPageViewSet.as_view({'get': 'list'})
    ),
    path('api-create-card/', views.createCard.as_view()),
    path('api-create-volunteer/', views.createVolunteerProject.as_view()),
    path('categories/', views.CategoryViewSet.as_view({'get': 'list'})),
    path('funds/', views.FundViewSet.as_view({'get': 'list'})),
    path('volunteers/', views.VolunteerViewSet.as_view({'get': 'list'})),
    path('category_cards/<int:category_id>/<str:category>',
        views.CategoryCardsViewSet.as_view({'get': 'list'})
    ),
    path('fund_cards/<int:fund_id>/<str:fund>',
        views.FundCardsViewSet.as_view({'get': 'list'})
    ),
    path('volunteer/<int:id>',
        views.VolunteerPageViewSet.as_view({'get': 'list'})
    ), 
    
] + swagger
