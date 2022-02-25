from rest_framework import serializers
from accounts.models.admin_data_confirm import AdminDataConfirm


class AdminDataConfirmSerializer(serializers.ModelSerializer):

    class Meta:

        model = AdminDataConfirm

        fields = ['data_type',
                  'data_value',
                  'is_confirmed',
                  'comment',
                  'date_time',
                  'id']

        read_only_fields = ['id']
