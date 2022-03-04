from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from accounts.models.profiles.business import BusinessProfile
from accounts.models.system_data_confirm import SystemDataConfirm

from business_service.models.business_product import BusinessProduct
from business_skill.models.business_skill import BusinessSkill
from business_skill.models.business_specialty import BusinessSpecialty

from accounts.model_serializers.view.public_user_register import PublicUserRegisterViewSerializer
from business_skill.model_serializers.view.business_skill import BusinessSkillViewSerializer
from business_service.model_serializers.view.public.business_product import PublicBusinessProductViewSerializer
from business_skill.model_serializers.business_specialty import BusinessSpecialtySerializer



class PublicBusinessProfileViewSerializer(serializers.ModelSerializer):

    business_skills = SerializerMethodField('get_skills')
    business_products = SerializerMethodField('get_products')
    business_specialties = serializers.SerializerMethodField('get_specialties')
    user = SerializerMethodField()

    class Meta:

        model = BusinessProfile
        fields = ['user',
                  'id',
                  'bio',
                  'company_name',
                  'company_phone_number',
                  'service_number',
                  'service_rate',
                  'business_skills',
                  'business_products',
                  'business_specialties']


    def get_products(self, obj):


        products = BusinessProduct.objects.filter(business_profile=obj)

        for product in products:

            cnt = ContentType.objects.get_for_model(product)
            admin_confirm = get_object_or_404(SystemDataConfirm,
                                              target_ct=cnt,
                                              target_id=product.id)

            if admin_confirm.is_confirmed is False:
                products = products.exclude(id=product.id)

        serializer = PublicBusinessProductViewSerializer(instance=products, many=True)
        return serializer.data

    def get_skills(self, obj):

        skills = BusinessSkill.objects.filter(score__gt=0, business_profile=obj)
        serializer = BusinessSkillViewSerializer(instance=skills, many=True)
        return serializer.data

    def get_user(self, obj):

        user = obj.user
        serializer = PublicUserRegisterViewSerializer(instance=user)
        return serializer.data

    def get_specialties(self, obj):

        specialties = BusinessSpecialty.objects.filter(business_profile=obj)

        serializer = BusinessSpecialtySerializer(specialties, many=True)

        return serializer.data
