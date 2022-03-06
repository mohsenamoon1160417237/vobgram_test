from accounts.models.UserRegistration import UserRegistration
from rest_framework import serializers



class RegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserRegistration
        fields = ['phone_number', 'password', 'user_type']

    def update(self, instance, validated_data):

        user_type = validated_data['user_type']
        instance.set_password(validated_data['password'])
        instance.user_type = user_type
        instance.registered = True
        instance.save()
        return instance
