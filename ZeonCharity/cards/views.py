from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from .services import stats, stats_proba
from rest_framework.decorators import action


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


class FundViewSet(viewsets.ModelViewSet):
    queryset = Fund.objects.all()
    serializer_class = FundSerializer


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer


class VolunteerPageViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer

    def list(self, request, *args, **kwargs):
        queryset = Volunteer.objects.filter(id=kwargs['id'])

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FundPageViewSet(viewsets.ModelViewSet):
    queryset = Fund.objects.all()
    serializer_class = FundSerializer

    def list(self, request, *args, **kwargs):
        queryset = Fund.objects.filter(id=kwargs['id'])

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def list(self, request, *args, **kwargs):
        queryset = Card.objects.filter(id=kwargs['id'])

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class createCard(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def post(self, request):
        try:
            data = request.data
            current_category = Category.objects.get(pk=data['category'])
            data['category'] = current_category
            new_obj = Card.objects.create(**data)

            new_obj.save()
            
            return Response({'info': 'successfuly added'})
        except:
            return Response({'info': 'invalid data!'})


class createVolunteerProject(generics.CreateAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer

    def post(self, request):
        try:
            data = request.data
            new_obj = Card.objects.create(**data)

            new_obj.save()
            
            return Response({'info': 'successfuly added'})
        except:
            return Response({'info': 'invalid data!'})


class CategoryCardsViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def list(self, request, *args, **kwargs):
        queryset = Card.objects.filter(category_id=kwargs['category_id'])

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FundCardsViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def list(self, request, *args, **kwargs):
        queryset = Card.objects.filter(fund_id=kwargs['fund_id'])

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)     


class CalculateStat(generics.ListAPIView):
    def get(self, request):
        return Response({'stats': stats(), 'stats_proba': stats_proba()})
