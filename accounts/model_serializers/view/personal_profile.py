from rest_framework import serializers

from accounts.models.profiles.personal import PersonalProfile


class PersonalProfileViewSerializer(serializers.ModelSerializer):

    class Meta:

        model = PersonalProfile
        fields = ['first_name',
                  'last_name',
                  'email',
                  'username',
                  'id']
