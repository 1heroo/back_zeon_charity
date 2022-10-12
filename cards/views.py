from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action
from hashlib import md5
from user.serializers import RegUserSerializer
from rest_framework.parsers import FormParser, MultiPartParser

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


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class createCategory(generics.CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#     def post(self, request):
#         try:
#             data = request.data
#             new_obj = Card.objects.create(**data)
#
#             new_obj.save()
#
#             return Response({'info': 'successfuly added'})
#         except:
#             return Response({'info': 'invalid data!'})

class FundraisingCardAPIView(generics.GenericAPIView):
    serializer_class = FundraisingCardSerializer
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request):
        print(request.data)
        return Response('asd')

# class FundraisingCardViewSet(viewsets.ModelViewSet):
#     queryset = FundraisingCard.objects.all()
#     serializer_class = FundraisingCardSerializer
#     parser_classes = (FormParser, MultiPartParser)
#     # http_method_names = ['get']
#     # permission_classes = (IsAuthenticated,)
#
#     def post(self, request):
#         print(request.data)
#         serializer = FundraisingCardSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response('asdd')
#         return Response('sad')
#         # # images = request.data.pop('images')
#         # img_serializer = FundraisingCardSerializedSerializer(data=request.data)
#         # # data = request.data
#         return Response({'response': 'asd'})
#
#     # def get_parsers(self):
#     #     if getattr(self, 'swagger_fake_view', False):
#     #         return []
#     #
#     #     return (FormParser, MultiPartParser) # super().get_parsers()
#

class VolunteeringCardViewSet(viewsets.ModelViewSet):
    queryset = VolunteeringCard.objects.all()
    serializer_class = VolunteeringCardSerializer
    # http_method_names = ['get']
    permission_classes = (IsAuthenticated,)


# class CategoryCardsViewSet(viewsets.ModelViewSet):
#     queryset = FundraisingCard.objects.all()
#     serializer_class = FundraisingCardSerializer
#
#     def list(self, request, *args, **kwargs):
#         queryset = FundraisingCard.objects.filter(category_id=kwargs['category_id'])
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

#
# class CalculateStat(generics.ListAPIView):
#     def get(self, request):
#         return Response({'stats': stats(), 'stats_proba': stats_proba()})

class paymentHandler(generics.CreateAPIView):
    queryset = Donations.objects.all()
    serializer_class = DonationSerializer

    def post(self, request):
        data_req = request.data
        card_id = data_req['card']
        user_id = data_req['user']
        pg_order_id = 111
        pg_merchant_id = 535456
        pg_amount = data_req['donation_amnt']
        pg_description = 'test-bega'
        pg_salt = 'some-salt'

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


class CardApply(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CardApplySerializer

    def post(self, request):
        data = request.data
        data['user'] = request.user
        request = CardApplyModel(**data)
        request.save()
        return Response({'response': 'Successfully created new apply'})
