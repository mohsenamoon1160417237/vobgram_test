from rest_framework import serializers

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from business_service.models.business_product import BusinessProduct
from business_service.models.business_product_step import BusinessProductStep

from accounts.models.system_data_confirm import SystemDataConfirm

from accounts.model_serializers.system_data_confirm import SystemDataConfirmSerializer
from .business_product_step import AdminBusinessProductStepViewSerializer


class AdminBusinessProductViewSerializer(serializers.ModelSerializer):

    product_steps = serializers.SerializerMethodField()
    product_conf = serializers.SerializerMethodField()

    class Meta:

        model = BusinessProduct
        fields = ['title',
                  'description',
                  'total_up_votes',
                  'id',
                  'product_steps',
                  'product_conf']

    def get_product_steps(self, obj):

        product_steps = BusinessProductStep.objects.filter(business_product=obj)

        serializer = AdminBusinessProductStepViewSerializer(instance=product_steps, many=True)
        return serializer.data

    def get_product_conf(self, obj):

        cnt = ContentType.objects.get_for_model(obj)

        admin_conf = get_object_or_404(SystemDataConfirm,
                                       target_ct=cnt,
                                       target_id=obj.id)

        serializer = SystemDataConfirmSerializer(admin_conf)
        return serializer.data
