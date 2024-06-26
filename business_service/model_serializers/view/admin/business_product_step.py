from rest_framework import serializers

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from business_service.models.business_product_step import BusinessProductStep
from accounts.models.system_data_confirm import SystemDataConfirm

from accounts.model_serializers.system_data_confirm import SystemDataConfirmSerializer


class AdminBusinessProductStepViewSerializer(serializers.ModelSerializer):

    product_step_conf = serializers.SerializerMethodField()

    class Meta:

        model = BusinessProductStep
        fields = ['note',
                  'step_url',
                  'from_date',
                  'to_date',
                  'step_number',
                  'id',
                  'product_step_conf']

    def get_product_step_conf(self, obj):

        cnt = ContentType.objects.get_for_model(obj)

        admin_conf = get_object_or_404(SystemDataConfirm,
                                       target_ct=cnt,
                                       target_id=obj.id)

        serializer = SystemDataConfirmSerializer(admin_conf)

        return serializer.data
