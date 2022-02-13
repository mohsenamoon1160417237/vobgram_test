from rest_framework import serializers

from business_service.models.business_product_step import BusinessProductStep


class BusinessProductStepViewSerializer(serializers.ModelSerializer):

    class Meta:

        model = BusinessProductStep
        fields = ['note',
                  'step_url',
                  'from_date',
                  'to_date',
                  'step_number',
                  'id']
