from rest_framework import serializers
from accounts.models.profiles.business import BusinessProfile
from django.shortcuts import get_object_or_404
from accounts.models.UserRegistration import UserRegistration
from accounts.models.admin_data_confirm import AdminDataConfirm
from .utils.create_admin_data_confirm import create_admin_data_confirm


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

        company_name_admin = get_object_or_404(AdminDataConfirm,
                                               business_profile=instance,
                                               data_type='company_name',
                                               is_latest=True)

        if company_name_admin.admin_profile is not None:
            company_name_admin.is_latest = False
            company_name_admin.save()
            create_admin_data_confirm(instance, 'company_name', validated_data['company_name'])
        else:
            company_name_admin.data_value = validated_data['company_name']
            company_name_admin.save()

        instance.company_phone_number = validated_data.get('company_phone_number', instance.company_phone_number)

        company_phone_number_admin = get_object_or_404(AdminDataConfirm,
                                                       business_profile=instance,
                                                       data_type='company_phone_number',
                                                       is_latest=True)

        if company_phone_number_admin.admin_profile is not None:
            company_phone_number_admin.is_latest = False
            company_phone_number_admin.save()
            create_admin_data_confirm(instance, 'company_phone_number', validated_data['company_phone_number'])
        else:
            company_phone_number_admin.data_value = validated_data['company_phone_number']
            company_phone_number_admin.save()

        instance.bio = validated_data.get('bio', instance.bio)

        instance.save()
        return instance
