from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from accounts.models.profiles.business import BusinessProfile
from business_service.models.business_product import BusinessProduct
from business_service.models.business_skill import BusinessSkill

from accounts.model_serializers.view.private_user_register import PrivateUserRegisterViewSerializer
from business_service.model_serializers.view.business_skill import BusinessSkillViewSerializer
from business_service.model_serializers.view.private.business_product import PrivateBusinessProductViewSerializer



class PrivateBusinessProfileViewSerializer(serializers.ModelSerializer):

    business_skills = SerializerMethodField('get_skills')
    business_products = SerializerMethodField('get_products')
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
                  'business_products']

    def get_products(self, obj):

        products = BusinessProduct.objects.filter(business_profile=obj)
        serializer = PrivateBusinessProductViewSerializer(instance=products, many=True)
        return serializer.data

    def get_skills(self, obj):

        skills = BusinessSkill.objects.filter(business_profile=obj)
        serializer = BusinessSkillViewSerializer(instance=skills, many=True)
        return serializer.data

    def get_user(self, obj):

        user = obj.user
        serializer = PrivateUserRegisterViewSerializer(instance=user)
        return serializer.data
