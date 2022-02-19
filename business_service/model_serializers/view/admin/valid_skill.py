from rest_framework import serializers
from business_service.models.valid_skill import ValidSkill


class AdminValidSkillViewSerializer(serializers.ModelSerializer):

    class Meta:

        model = ValidSkill
        fields = ['title', 'description', 'id']

