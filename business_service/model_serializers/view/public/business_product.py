from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from business_service.models.business_product import BusinessProduct
from business_service.models.business_product_step import BusinessProductStep

from business_service.model_serializers.view.business_product_step import BusinessProductStepViewSerializer
from business_service.model_serializers.view.business_product_vote import BusinessProductVoteViewSerializer

from accounts.model_serializers.system_data_confirm import SystemDataConfirmSerializer
from accounts.models.system_data_confirm import SystemDataConfirm


class PublicBusinessProductViewSerializer(serializers.ModelSerializer):

    product_steps = serializers.SerializerMethodField()
    product_votes = serializers.SerializerMethodField('get_votes')

    class Meta:

        model = BusinessProduct
        fields = ['title',
                  'description',
                  'total_up_votes',
                  'id',
                  'product_steps']

    def get_admin_data(self, obj):

        cnt = ContentType.objects.get_for_model(obj)
        admin_confirm = get_object_or_404(SystemDataConfirm,
                                          target_ct=cnt,
                                          target_id=obj.id)

        serializer = SystemDataConfirmSerializer(instance=admin_confirm)
        return serializer.data

    def get_product_steps(self, obj):

        product_steps = BusinessProductStep.objects.filter(business_product=obj)

        for product_step in product_steps:

            cnt = ContentType.objects.get_for_model(product_step)

            admin_confirm = get_object_or_404(SystemDataConfirm,
                                              target_ct=cnt,
                                              target_id=product_step.id,
                                              is_confirmed=True,
                                              is_latest=True)

            if admin_confirm.is_confirmed is False:

                product_steps = product_steps.exclude(id=product_step.id)

        serializer = BusinessProductStepViewSerializer(instance=product_steps, many=True)
        return serializer.data

    def get_votes(self, obj):

        votes = obj.product_votes.all()
        serializer = BusinessProductVoteViewSerializer(votes, many=True)
        return serializer.data
