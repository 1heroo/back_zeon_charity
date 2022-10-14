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


class FundraisingCardAPIView(generics.GenericAPIView):

    serializer_class = FundraisingCardSerializer

    def post(self, request):
        print(request.data)
        return Response(request.data)

# class FundraisingCardViewSet(viewsets.ModelViewSet):
#     queryset = FundraisingCard.objects.all()
#     serializer_class = FundraisingCardSerializer
#     parser_classes = (FormParser, MultiPartParser)
#     # http_method_names = ['get']
#     # permission_classes = (IsAuthenticated,)
#
    # def post(self, request):
    #     print(request.data)
    #     serializer = FundraisingCardSerializer(data=request.data, )
    #     if serializer.is_valid():
    #         return Response('asd')
    #     return Response('sad')
        # # images = request.data.pop('images')
        # img_serializer = FundraisingCardSerializedSerializer(data=request.data)
        # # data = request.data
        # return Response({'response': 'asd'})


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
