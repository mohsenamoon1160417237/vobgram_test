from rest_framework import serializers

from accounts.models.profiles.customer import CustomerProfile
from .public_user_register import PublicUserRegisterViewSerializer


class CustomerProfileViewSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:

        model = CustomerProfile
        fields = ['user',
                  'id']

    def get_user(self, obj):

        user = obj.user
        serializer = PublicUserRegisterViewSerializer(user)
        return serializer.data
    