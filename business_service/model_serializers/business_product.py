from rest_framework import serializers

from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from accounts.model_serializers.utils.create_admin_data_confirm import create_admin_data_confirm
from business_service.model_serializers.utils.update_admin_confirm import update_admin_confirm

from business_service.models.business_product import BusinessProduct
from business_service.models.business_skill import BusinessSkill

from accounts.models.profiles.business import BusinessProfile
from accounts.models.admin_data_confirm import AdminDataConfirm


class BusinessProductSerializer(serializers.ModelSerializer):

    business_skill_id = serializers.IntegerField()
    business_profile_id = serializers.IntegerField()

    class Meta:

        model = BusinessProduct
        fields = ['business_skill_id',
                  'business_profile_id',
                  'title',
                  'description']

    def create(self, validated_data):

        business_profile = get_object_or_404(BusinessProfile,
                                             id=validated_data['business_profile_id'])
        business_skill = get_object_or_404(BusinessSkill,
                                           id=validated_data['business_skill_id'])
        try:
            admin_confirm = create_admin_data_confirm(business_profile, 'business_product', validated_data['title'])

            product = BusinessProduct.objects.create(business_profile=business_profile,
                                                     business_skill=business_skill,
                                                     title=validated_data['title'],
                                                     description=validated_data['description'],
                                                     admin_data_confirm=admin_confirm)
            return product

        except IntegrityError:
            raise serializers.ValidationError({'error': 'You already have a product with this title'})

    def update(self, instance, validated_data):

        business_skill = get_object_or_404(BusinessSkill,
                                           id=validated_data['business_skill_id'])
        instance.business_skill = business_skill
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)

        try:
            instance.save()
            update_admin_confirm(instance.business_profile, 'business_product', validated_data['title'])

            return instance
        
        except IntegrityError:
            raise serializers.ValidationError({'error': 'You already have a product with this title'})
