from rest_framework import serializers

from accounts.models.admin_data_confirm import AdminDataConfirm


class AdminDataConfirmViewSerializer(serializers.ModelSerializer):

    class Meta:

        model = AdminDataConfirm
        fields = ['is_confirmed']
