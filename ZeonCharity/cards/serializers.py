from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'photo')


class CardImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardImage
        fields = ['photo',]


class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = (
            'title',
            'description',
            'photo',
            'total_raised',
            'total_helpers'
        )


class CardSerializer(serializers.ModelSerializer):
    card_images = CardImageSerializer(many=True, read_only=True)
    class Meta:
        model = Card
        fields = (
            'title',
            'category',
            'description',
            'target_amnt',
            'total_amnt',
            'deadline',
            'is_urgent',
            'is_approved',
            'total',
            'card_images'
        )
