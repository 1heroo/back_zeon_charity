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
from django.conf.urls.static import static
from ZeonCharity import settings

urlpatterns = i18n_patterns(
    path('', include('cards.urls')),
    path('admin/', admin.site.urls),
    path('user-auth/', include('user.urls')),
    path('rosetta/', include('rosetta.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    path('search/', views.SearchModelView.as_view({'get': 'list'})),

    # path('payment/', views.paymentHandler.as_view()),
    path('payments/', include('payments.urls')),

) + swagger + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

