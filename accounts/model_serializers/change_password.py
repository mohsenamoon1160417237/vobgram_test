from rest_framework import serializers
from accounts.models.UserRegistration import UserRegistration



class ChangePasswordSerializer(serializers.ModelSerializer):

    current_password = serializers.CharField(max_length=30)

    class Meta:

        model = UserRegistration
        fields = ['password', 'current_password']

    def validate_current_password(self, value):

        if not self.instance.check_password(value):
            raise serializers.ValidationError("wrong password")
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()
        return instance
