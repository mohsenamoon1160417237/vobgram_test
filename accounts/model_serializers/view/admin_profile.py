from rest_framework import serializers

from accounts.models.profiles.admin import AdminProfile

from accounts.model_serializers.view.public_user_register import PublicUserRegisterViewSerializer


class AdminProfileViewSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:

        model = AdminProfile
        fields = ['user',
                  'id']

    def get_user(self, obj):

        user = obj.user
        serializer = PublicUserRegisterViewSerializer(user)
        return serializer.data
    