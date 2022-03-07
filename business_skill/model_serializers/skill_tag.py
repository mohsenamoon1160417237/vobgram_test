from rest_framework import serializers

from business_skill.models.skill_tag import SkillTag


class SkillTagSerializer(serializers.ModelSerializer):

    class Meta:

        model = SkillTag
        fields = ['title',
                  'id']
