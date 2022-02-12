from rest_framework import serializers
from django.shortcuts import get_object_or_404

from accounts.models.profiles.business import BusinessProfile
from accounts.models.UserRegistration import UserRegistration

from .utils.create_admin_data_confirm import create_admin_data_confirm
from business_service.model_serializers.utils.check_admin_confirm_latest import check_admin_confirm_latest


class BusinessProfileSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField()

    class Meta:

        model = BusinessProfile
        fields = ['user_id',
                  'company_name',
                  'company_phone_number',
                  'bio']

    def create(self, validated_data):

        user = get_object_or_404(UserRegistration, id=validated_data['user_id'])
        business_profile = BusinessProfile.objects.create(user=user,
                                                          company_name=validated_data['company_name'],
                                                          company_phone_number=validated_data['company_phone_number'],
                                                          bio=validated_data['bio'])

        create_admin_data_confirm(business_profile, 'company_name', validated_data['company_name'])
        create_admin_data_confirm(business_profile, 'company_phone_number', validated_data['company_phone_number'])

        return business_profile

    def update(self, instance, validated_data):

        instance.company_name = validated_data.get('company_name', instance.company_name)

        check_admin_confirm_latest(instance, 'company_name', validated_data['company_name'])

        instance.company_phone_number = validated_data.get('company_phone_number', instance.company_phone_number)

        check_admin_confirm_latest(instance, 'company_phone_number', validated_data['company_phone_number'])

        instance.bio = validated_data.get('bio', instance.bio)

        instance.save()
        return instance
