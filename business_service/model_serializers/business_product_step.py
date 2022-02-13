from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from business_service.models.business_product_step import BusinessProductStep
from business_service.models.business_product import BusinessProduct
from accounts.models.admin_data_confirm import AdminDataConfirm



class BusinessProductStepSerializer(serializers.ModelSerializer):

    business_product_id = serializers.IntegerField()

    class Meta:

        model = BusinessProductStep
        fields = ['business_product_id',
                  'note',
                  'step_url',
                  'from_date',
                  'to_date']

    def create(self, validated_data):

        business_product = get_object_or_404(BusinessProduct,
                                             id=validated_data['business_product_id'])
        business_product.max_step_number += 1
        business_product.save()

        max_step_number = business_product.max_step_number

        product_step = BusinessProductStep.objects.create(business_product=business_product,
                                                          note=validated_data['note'],
                                                          step_url=validated_data['step_url'],
                                                          from_date=validated_data['from_date'],
                                                          to_date=validated_data['to_date'],
                                                          step_number=max_step_number
                                                          )

        AdminDataConfirm.objects.create(target=product_step)
        return product_step

    def update(self, instance, validated_data):

        instance.note = validated_data['note']
        instance.step_url = validated_data['step_url']
        instance.from_date = validated_data['from_date']
        instance.to_date = validated_data['to_date']
        instance.save()

        return instance
