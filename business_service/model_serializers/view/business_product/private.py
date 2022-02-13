from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from business_service.models.business_product import BusinessProduct
from business_service.models.business_product_step import BusinessProductStep

from business_service.model_serializers.view.business_product_step import BusinessProductStepViewSerializer

from accounts.model_serializers.view.admin_data_confirm import AdminDataConfirmViewSerializer
from accounts.models.admin_data_confirm import AdminDataConfirm


class PrivateBusinessProductViewSerializer(serializers.ModelSerializer):

    product_steps = serializers.SerializerMethodField()

    class Meta:

        model = BusinessProduct
        fields = ['title',
                  'description',
                  'total_up_votes',
                  'id',
                  'product_steps']

    def get_product_steps(self, obj):

        product_steps = BusinessProductStep.objects.filter(business_product=obj)

        serializer = BusinessProductStepViewSerializer(instance=product_steps, many=True)
        return serializer.data
