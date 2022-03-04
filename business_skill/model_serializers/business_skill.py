from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.db import IntegrityError

from business_skill.models.business_skill import BusinessSkill
from accounts.models.profiles.business import BusinessProfile
from business_skill.models.valid_skill import ValidSkill


class BusinessSkillSerializer(serializers.ModelSerializer):

    valid_skill_id = serializers.IntegerField()
    business_profile_id = serializers.IntegerField()

    class Meta:

        model = BusinessSkill
        fields = ['valid_skill_id', 'business_profile_id']

    def create(self, validated_data):

        valid_skill = get_object_or_404(ValidSkill, id=validated_data['valid_skill_id'])
        business_profile = get_object_or_404(BusinessProfile, id=validated_data['business_profile_id'])

        try:
            business_skill = BusinessSkill.objects.create(business_profile=business_profile,
                                                          valid_skill=valid_skill)
            valid_skill.selected_number += 1
            valid_skill.save()
            return business_skill

        except IntegrityError:
            raise serializers.ValidationError({'error': 'You have already chosen this skill'})
