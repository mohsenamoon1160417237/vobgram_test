from rest_framework import serializers
from accounts.models.system_data_confirm import SystemDataConfirm


class SystemDataConfirmSerializer(serializers.ModelSerializer):

    class Meta:

        model = SystemDataConfirm

        fields = ['data_type',
                  'data_value',
                  'is_confirmed',
                  'comment',
                  'date_time',
                  'id']

        read_only_fields = ['id']
