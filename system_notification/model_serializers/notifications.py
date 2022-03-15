from rest_framework import serializers

from system_notification.models.system_notification import SystemNotification


class SystemNotificationSerializer(serializers.ModelSerializer):

    class Meta:

        model = SystemNotification
        fields = ['message',
                  'date_time',
                  'seen']
