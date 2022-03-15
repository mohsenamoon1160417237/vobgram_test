import datetime

from system_notification.models.system_notification import SystemNotification
from system_notification.model_serializers.notifications import SystemNotificationSerializer


class SystemNotificationManager:

    def __init__(self, receiver, message=None):

        self.receiver = receiver
        self.message = message

    def doCreate(self):

        notif = SystemNotification.objects.create(receiver=self.receiver,
                                                  message=self.message,
                                                  date_time=datetime.datetime.now())
        return notif

    def count_unseenNotifs(self):

        notifs = SystemNotification.objects.filter(receiver=self.receiver,
                                                   seen=False)
        count = notifs.count()
        return count

    def list_notifs(self):

        notifs = SystemNotification.objects.filter(receiver=self.receiver)
        serializer = SystemNotificationSerializer(notifs, many=True)
        return serializer.data
