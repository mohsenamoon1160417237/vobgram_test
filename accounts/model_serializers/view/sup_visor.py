from rest_framework import serializers

from accounts.models.profiles.sup_vs import SupVsProfile

from accounts.model_serializers.view.public_user_register import PublicUserRegisterViewSerializer


class SupVisorProfileViewSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:
        model = SupVsProfile
        fields = ['user',
                  'id']

    def get_user(self, obj):
        user = obj.user
        serializer = PublicUserRegisterViewSerializer(user)
        return serializer.data
