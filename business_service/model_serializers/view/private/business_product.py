from rest_framework import serializers

from business_service.models.business_product import BusinessProduct
from business_service.models.business_product_step import BusinessProductStep

from business_service.model_serializers.view.business_product_step import BusinessProductStepViewSerializer



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
