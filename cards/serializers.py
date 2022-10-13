from rest_framework import serializers
from .models import *


# class DonationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Donations
#         fields = ('user', 'card', 'donation_amnt')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'photo')


class FundraisingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundraisingCardImage
        fields = ['photo', ]


class FundraisingCardSerializer(serializers.ModelSerializer):
    images = FundraisingImageSerializer(many=True, read_only=True)

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
            'images'
        )
        read_only_fields = (
            'is_urgent',
            'is_active',
            'is_approved',
            'images'
        )


class VolunteeringImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteeringCardImage
        fields = ['photo', ]


class VolunteeringDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteeringCardDocument
        fields = ['document', ]


class VolunteeringLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteeringCardLocation
        fields = ['location', ]


class VolunteeringCardSerializer(serializers.ModelSerializer):
    images = VolunteeringImageSerializer(many=True, read_only=True)
    documents = VolunteeringDocumentSerializer(many=True, read_only=True)
    locations = VolunteeringLocationSerializer(many=True, read_only=True)

    class Meta:
        model = VolunteeringCard

        fields = (
            'title',
            'description',
            'start_dt',
            'end_dt',
            'contacts',
            'is_active',
            'images',
            'documents',
            'locations'
        )
        read_only_fields = (
            'images',
            'documents',
            'locations'
        )
