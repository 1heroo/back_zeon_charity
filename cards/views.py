from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action
from hashlib import md5
from user.serializers import RegUserSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend
from django.core.paginator import Paginator

from rest_framework.decorators import api_view
from rest_framework import status


# def pay(request):
#     print 'RECEIVED REQUEST: ' + request.method
#     if request.method == 'POST':
#         print 'Hello'


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class createCategory(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request):
        try:
            data = request.data
            new_obj = Card.objects.create(**data)

            new_obj.save()
            
            return Response({'info': 'successfuly added'})
        except:
            return Response({'info': 'invalid data!'})


class FundraisingCardViewSet(viewsets.ModelViewSet):
    queryset = FundraisingCard.objects.all()
    serializer_class = FundraisingCardSerializer
    permission_classes = ()

    def list(self, request, *args, **kwargs):
        queryset = Card.objects.filter(id=kwargs['card_id'])

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class FundraisingCardsViewSet(viewsets.ModelViewSet):
    queryset = FundraisingCard.objects.all()
    serializer_class = FundraisingCardSerializer
    permission_classes = (IsAuthenticated,)

class createFundraisingCard(generics.CreateAPIView):
    queryset = FundraisingCard.objects.all()
    serializer_class = FundraisingCardSerializer

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


class CategoryCardsViewSet(viewsets.ModelViewSet):
    queryset = FundraisingCard.objects.all()
    serializer_class = FundraisingCardSerializer

    def list(self, request, *args, **kwargs):
        queryset = Card.objects.filter(category_id=kwargs['category_id'])

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
 


class CalculateStat(generics.ListAPIView):
    def get(self, request):
        return Response({'stats': stats(), 'stats_proba': stats_proba()})


class paymentHandler(generics.CreateAPIView):

    queryset = Donations.objects.all()
    serializer_class = DonationSerializer
    def post(self, request):
        data_req = request.data
        card_id = data_req['card']
        user_id = data_req['user']
        pg_order_id=111
        pg_merchant_id=535456
        pg_amount=data_req['donation_amnt']
        pg_description='test-bega'
        pg_salt='some-salt'

        data = f'init_payment.php;{pg_amount};{pg_description};{pg_merchant_id};{pg_order_id};{pg_salt};LeFnP16MP6AU6YKc'
        ps_sig = md5(data.encode('utf-8')).hexdigest()

        post_url = f'https://api.paybox.money/init_payment.php?pg_order_id={pg_order_id}&pg_merchant_id={pg_merchant_id}&pg_amount={pg_amount}&pg_description={pg_description}&pg_salt={pg_salt}&pg_sig={ps_sig}'
        new_donation = Donations.objects.create(
            user=MyUser.objects.get(pk=user_id),
            card=Card.objects.get(pk=card_id),
            donation_amnt=pg_amount
        )
        return Response({'response': post_url}) 

class SearchModelView(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = RegUserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name']