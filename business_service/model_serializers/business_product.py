from rest_framework import serializers

from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from accounts.model_serializers.utils.create_admin_data_confirm import create_admin_data_confirm
from admin_action.views.utils.check_system_confirm_latest import check_system_confirm_latest

from business_service.models.business_product import BusinessProduct
from business_skill.models.business_skill import BusinessSkill

from accounts.models.profiles.business import BusinessProfile


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

            product = BusinessProduct.objects.create(business_profile=business_profile,
                                                     business_skill=business_skill,
                                                     title=validated_data['title'],
                                                     description=validated_data['description'])

            create_admin_data_confirm(product, business_profile, None)
            return product

        except IntegrityError:
            raise serializers.ValidationError({'error': 'You already have a product with this title'})

    def update(self, instance, validated_data):

        business_profile = get_object_or_404(BusinessProfile,
                                             id=validated_data['business_profile_id'])

        business_skill = get_object_or_404(BusinessSkill,
                                           id=validated_data['business_skill_id'])
        instance.business_skill = business_skill
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)

        try:

            check_system_confirm_latest(instance, business_profile, None)

            instance.save()
            return instance
        
        except IntegrityError:
            raise serializers.ValidationError({'error': 'You already have a product with this title'})
