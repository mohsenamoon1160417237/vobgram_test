from rest_framework import serializers
from business_service.models.business_skill import BusinessSkill
from business_service.model_serializers.valid_skill import ValidSkillSerializer


class BusinessSkillViewSerializer(serializers.ModelSerializer):

    valid_skill = ValidSkillSerializer()

    class Meta:

        model = BusinessSkill
        fields = ['score', 'valid_skill', 'id']
