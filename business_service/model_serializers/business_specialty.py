from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from accounts.model_serializers.utils.create_admin_data_confirm import create_admin_data_confirm

from business_service.models.business_specialty import BusinessSpecialty
from accounts.models.profiles.business import BusinessProfile

from .utils.check_admin_confirm_latest import check_admin_confirm_latest


class BusinessSpecialtySerializer(serializers.ModelSerializer):

    business_profile_id = serializers.IntegerField()

    class Meta:

        model = BusinessSpecialty
        fields = ['business_profile_id',
                  'title',
                  'note',
                  'education_institute_name']

    def create(self, validated_data):

        business_profile = get_object_or_404(BusinessProfile, id=validated_data['business_profile_id'])

        try:

            specialty = BusinessSpecialty.objects.create(business_profile=business_profile,
                                                         title=validated_data['title'],
                                                         note=validated_data['note'],
                                                         education_institute_name=validated_data['education_institute_name'])

            business_profile = specialty.business_profile

            create_admin_data_confirm(specialty, business_profile, None)

            return specialty

        except IntegrityError:

            raise serializers.ValidationError({'error': 'You have a similar specialty with this title'})

    def update(self, instance, validated_data):

        business_profile = get_object_or_404(BusinessProfile, id=validated_data['business_profile_id'])

        instance.title = validated_data['title']
        instance.note = validated_data['note']
        instance.education_institute_name = validated_data['education_institute_name']

        try:
            instance.save()
            check_admin_confirm_latest(instance, business_profile, None)

            return instance

        except IntegrityError:

            raise serializers.ValidationError({'error': 'You have a similar specialty with this title'})
