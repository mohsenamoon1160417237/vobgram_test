from rest_framework import serializers

from business_skill.models.valid_skill import ValidSkill
from accounts.model_serializers.utils.create_admin_data_confirm import create_admin_data_confirm


class ValidSkillSerializer(serializers.ModelSerializer):

    class Meta:

        model = ValidSkill
        fields = ['title',
                  'description',
                  'id']

        read_only_fields = ['id']

    def create(self, validated_data):

        valid_skill = ValidSkill.objects.create(title=validated_data['title'],
                                                description=validated_data['description'])
        create_admin_data_confirm(valid_skill, None, None)

        return valid_skill
