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
        fields = ['photo', ]


class FundraisingCardSerializer(serializers.ModelSerializer):
    card_images = CardImageSerializer(many=True, read_only=True)

    class Meta:
        model = FundraisingCard
        fields = (
            'title',
            'category',
            'description',
            'target_amnt',
            'deadline',
            'is_urgent',
            'is_active',
            'is_approved',
            'total',
            'contacts',
            'card_images'
        )


class VolunteeringCardSerializer(serializers.ModelSerializer):
    card_images = CardImageSerializer(many=True, read_only=True)

    class Meta:
        model = VolunteeringCard
        fields = (
            'title',
            'description',
            'location',
            'start_dt',
            'end_dt',
            'responsibility',
            'requirements',
            'contacts',
            'is_active',
            'card_images'
        )
