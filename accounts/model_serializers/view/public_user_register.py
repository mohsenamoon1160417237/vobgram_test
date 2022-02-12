from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from django.shortcuts import get_object_or_404

from accounts.models.UserRegistration import UserRegistration
from accounts.models.profiles.personal import PersonalProfile
from accounts.model_serializers.view.personal_profile import PersonalProfileViewSerializer


class PublicUserRegisterViewSerializer(serializers.ModelSerializer):

    personal_profile = SerializerMethodField()

    class Meta:

        model = UserRegistration
        fields = ['personal_profile']

    def get_personal_profile(self, obj):

        profile = get_object_or_404(PersonalProfile, user=obj)
        serializer = PersonalProfileViewSerializer(instance=profile)
        return serializer.data
