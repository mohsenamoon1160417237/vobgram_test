from rest_framework import serializers
from accounts.models.profiles.personal import PersonalProfile
from django.shortcuts import get_object_or_404
from accounts.models.UserRegistration import UserRegistration


class ProfileFirstStepSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField()

    class Meta:

        model = PersonalProfile
        fields = ['first_name', 'last_name', 'user_id', 'email', 'username']

    def create(self, validated_data):

        user = get_object_or_404(UserRegistration, id=validated_data['user_id'])
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        username = validated_data['username']
        profile = PersonalProfile.objects.create(user=user,
                                                 first_name=first_name,
                                                 last_name=last_name,
                                                 email=email,
                                                 username=username)
        return profile

    def update(self, instance, validated_data):

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
