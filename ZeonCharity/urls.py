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
from .yasg import urlpatterns as swagger
from cards import views
from django.conf.urls.i18n import i18n_patterns
from rest_framework import routers
from django.conf.urls.static import static
from ZeonCharity import settings

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'cards', views.FundraisingCardViewSet)


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('user-auth/', include('user.urls')),
    path('rosetta/', include('rosetta.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('cards/', views.FundraisingCardsViewSet.as_view({'get': 'list'})),
    path(
        'cards/<int:card_id>',
        views.FundraisingCardViewSet.as_view({'get': 'list'})
    ), 
    path('cards/create', views.createFundraisingCard.as_view()),

    path('categories/', views.CategoryViewSet.as_view({'get': 'list'})),
    path('categories/create', views.createCategory.as_view()),

    path('search/', views.SearchModelView.as_view({'get': 'list'})),

    path('cards/category/<int:category_id>/',
        views.CategoryCardsViewSet.as_view({'get': 'list'})
    ),
    path('stats/', views.CalculateStat.as_view()),
    path('payment/', views.paymentHandler.as_view())
    
) + swagger + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
