from rest_framework import serializers
from business_service.models.valid_skill import ValidSkill
from accounts.model_serializers.utils.create_admin_data_confirm import create_admin_data_confirm


class ValidSkillSerializer(serializers.ModelSerializer):

    class Meta:

        model = ValidSkill
        fields = ['title', 'description']

    def create(self, validated_data):

        admin_confirm = create_admin_data_confirm(None, 'valid_skill', validated_data['title'])
        return ValidSkill.objects.create(title=validated_data['title'],
                                         description=validated_data['description'],
                                         admin_data_confirm=admin_confirm)
