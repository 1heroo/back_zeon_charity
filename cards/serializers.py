from rest_framework import serializers
from .models import *

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donations
        fields = ('user', 'card', 'donation_amnt')

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


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = (
            'title',
            'description',
            'photo',
            'city',
            'location',
            'start_dt',
            'end_dt',
            'responsibility',
            'requirements'
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
