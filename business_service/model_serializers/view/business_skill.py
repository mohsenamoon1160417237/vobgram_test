from rest_framework import serializers
from business_service.models.business_skill import BusinessSkill
from business_service.model_serializers.valid_skill import ValidSkillSerializer


class BusinessSkillViewSerializer(serializers.ModelSerializer):

    valid_skill = serializers.SerializerMethodField()

    class Meta:

        model = BusinessSkill
        fields = ['score', 'valid_skill', 'id']

    def get_valid_skill(self, obj):

        valid_skill = obj.valid_skill
        serializer = ValidSkillSerializer(valid_skill)
        return serializer.data
