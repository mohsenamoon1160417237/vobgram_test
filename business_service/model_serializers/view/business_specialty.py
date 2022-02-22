from rest_framework import serializers

from business_service.models.business_specialty import BusinessSpecialty



class BusinessSpecialtyViewSerializer(serializers.ModelSerializer):

    class Meta:

        model = BusinessSpecialty
        fields = ['title',
                  'note',
                  'education_institute_name',
                  'id']
