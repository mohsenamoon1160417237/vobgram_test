from rest_framework import serializers

from business_service.models.service_request import ServiceRequest

from accounts.model_serializers.view.personal_profile import PersonalProfileViewSerializer
from business_skill.model_serializers.valid_skill import ValidSkillSerializer


class CustomerServiceRequestViewSerializer(serializers.ModelSerializer):

    requester = serializers.SerializerMethodField()
    skills = serializers.SerializerMethodField()

    class Meta:

        model = ServiceRequest
        fields = ['requester',
                  'service_type',
                  'request_type',
                  'skills',
                  'title',
                  'note',
                  'min_price',
                  'max_price',
                  'max_days',
                  'finished',
                  'id']

        read_only_fields = ['request_type']

    def get_requester(self, obj):

        requester = obj.requester

        serializer = PersonalProfileViewSerializer(requester)
        return serializer.data

    def get_skills(self, obj):

        skills = obj.skill.all()
        serializer = ValidSkillSerializer(skills, many=True)
        return serializer.data
