from rest_framework import serializers
from business_service.models.business_product import BusinessProduct


class BusinessProductViewSerializer(serializers.ModelSerializer):

    class Meta:

        model = BusinessProduct
        fields = ['title', 'description', 'step', 'score']
        