from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from accounts.model_serializers.utils.create_admin_data_confirm import create_admin_data_confirm

from business_skill.models.business_specialty import BusinessSpecialty
from accounts.models.UserRegistration import UserRegistration

from admin_action.views.utils.check_system_confirm_latest import check_system_confirm_latest


class BusinessSpecialtySerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField()

    class Meta:

        model = BusinessSpecialty
        fields = ['user_id',
                  'title',
                  'note',
                  'education_institute_name',
                  'id']

        read_only_fields = ['id']

    def create(self, validated_data):

        user = get_object_or_404(UserRegistration, id=validated_data['user_id'])

        try:

            specialty = BusinessSpecialty.objects.create(user=user,
                                                         title=validated_data['title'],
                                                         note=validated_data['note'],
                                                         education_institute_name=validated_data['education_institute_name'])

            business_profile = specialty.business_profile

            create_admin_data_confirm(specialty, business_profile, None)

            return specialty

        except IntegrityError:

            raise serializers.ValidationError({'error': 'You have a similar specialty with this title'})

    def update(self, instance, validated_data):

        user = get_object_or_404(UserRegistration, id=validated_data['user_id'])

        instance.title = validated_data['title']
        instance.note = validated_data['note']
        instance.education_institute_name = validated_data['education_institute_name']

        try:
            instance.save()
            check_system_confirm_latest(instance, user, None)

            return instance

        except IntegrityError:

            raise serializers.ValidationError({'error': 'You have a similar specialty with this title'})
