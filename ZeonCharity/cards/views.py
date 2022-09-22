from django.shortcuts import render
from rest_framework import viewsets
from django.db.models import Sum
from .models import *
from .serializers import *


from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.core.paginator import Paginator

from rest_framework.decorators import api_view
from rest_framework import status


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def list(self, request, *args, **kwargs):
        queryset = Card.objects.filter(id=kwargs['id'])

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
