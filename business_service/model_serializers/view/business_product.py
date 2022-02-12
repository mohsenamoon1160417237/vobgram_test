from rest_framework import serializers
from django.shortcuts import get_object_or_404

from business_service.models.business_product import BusinessProduct
from accounts.model_serializers.view.admin_data_confirm import AdminDataConfirmViewSerializer
from accounts.models.admin_data_confirm import AdminDataConfirm


class BusinessProductViewSerializer(serializers.ModelSerializer):

    admin_data_confirm = serializers.SerializerMethodField('get_admin_data')

    class Meta:

        model = BusinessProduct
        fields = ['title',
                  'description',
                  'total_up_votes',
                  'id',
                  'admin_data_confirm']

    def get_admin_data(self, obj):

        business_profile = obj.business_profile
        admin_confirm = get_object_or_404(AdminDataConfirm,
                                          business_profile=business_profile,
                                          data_type='business_product',
                                          data_value=obj.title)

        serializer = AdminDataConfirmViewSerializer(instance=admin_confirm)
        return serializer.data
