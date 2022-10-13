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


class FundraisingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundraisingCardImage
        fields = '__all__'

    # def create(self, validated_data):
    #     photo = validated_data.pop('image')
    #     card = self.context.get('card')
    #     return FundraisingCardImage.objects.create(photo=photo, card=card)


class FundraisingCardSerializer(serializers.ModelSerializer):
    # images = serializers.ListField(
    #     child=serializers.ImageField()
    # )

    images = FundraisingImageSerializer(many=True)

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
            'deadline',
        )

        def create(self, validated_data):
            images = validated_data.pop('fund_card_images')
            print(f'ser {validated_data}')
            print(f'ser {images}')
            card = FundraisingCard.objects.create(**validated_data)
            for image_data in images:
                image, created = FundraisingCardImage.objects.get_or_create(photo=image_data, card=card)
            return card
        
        def update(self, instance, validated_data):
        
            instance.title = validated_data.get('title', instance.title)
            instance.content = validated_data.get('content', instance.content)
            instance.thumbnail = validated_data.get('thumbnail', instance.thumbnail)
            
            try:
                images_data = self.context.get('request').data.pop('images')
            except:
                images_data = None

            if images_data is not None:
                image_instance_list = []
                for image_data in images_data:
                    image, created = Image.objects.get_or_create(image=image_data)
                    image_instance_list.append(image)

                instance.images.set(image_instance_list)

            instance.save()  # why? see base class code; need to save() to make auto_now work
            return instance

        # def create(self, validated_data):
        #     image = validated_data.pop('images')
        #     card = FundraisingCard.objects.create(**validated_data)
        #
        #     image_serializer = FundraisingImageSerializer(data=image, context={'card': card})
        #     if image_serializer.is_valid(raise_exceptions=True):
        #         image_serializer.save()
        #     return card

        # def create(self, validated_data):
        #     # images = self.context.get('view').request.FILES
        #
        #     validated_data.pop('images')
        #     return super().create(validated_data)
        #
        #     # img_serializer = FundraisingImageSerializer(data=images, many=True)
        #     print(validated_data)
        #     return MyUser.objects.get(pk=1)

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


class CardApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = CardApplyModel
        fields = ('title', 'description', 'contacts', 'user')

        read_only_fields = ('user', )
