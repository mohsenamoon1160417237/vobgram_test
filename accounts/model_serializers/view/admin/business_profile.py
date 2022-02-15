from rest_framework import serializers

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from accounts.models.profiles.business import BusinessProfile
from accounts.models.admin_data_confirm import AdminDataConfirm

from accounts.model_serializers.view.admin_data_confirm import AdminDataConfirmViewSerializer



class AdminBusinessProfileViewSerializer(serializers.ModelSerializer):

    company_name_conf = serializers.SerializerMethodField()
    company_phone_number_conf = serializers.SerializerMethodField()

    class Meta:

        model = BusinessProfile
        fields = ['id',
                  'company_name',
                  'company_phone_number',
                  'bio',
                  'company_name_conf',
                  'company_phone_number_conf']

    def get_company_name_conf(self, obj):

        cnt = ContentType.objects.get_for_model(obj)

        admin_conf = get_object_or_404(AdminDataConfirm,
                                       target_ct=cnt,
                                       target_id=obj.id,
                                       data_type='company_name')

        serializer = AdminDataConfirmViewSerializer(admin_conf)
        return serializer.data

    def get_company_phone_number_conf(self, obj):

        cnt = ContentType.objects.get_for_model(obj)

        admin_conf = get_object_or_404(AdminDataConfirm,
                                       target_ct=cnt,
                                       target_id=obj.id,
                                       data_type='company_phone_number')

        serializer = AdminDataConfirmViewSerializer(admin_conf)
        return serializer.data
