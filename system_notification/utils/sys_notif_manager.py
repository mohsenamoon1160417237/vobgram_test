from system_notification.models.system_notification import SystemNotification
from system_notification.model_serializers.notifications import SystemNotificationSerializer



class SystemNotificationManager:

    def __init__(self, receiver, sender=None):

        self.receiver = receiver
        self.sender = sender

    def doCreate(self, notif_type, message=None, target=None, parent=None, url=None):

        notif = SystemNotification.objects.create(receiver=self.receiver,
                                                  sender=self.sender,
                                                  message=message,
                                                  notif_type=notif_type,
                                                  target=target,
                                                  parent=parent,
                                                  url=url)
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

    def obj_quest(self, message, target):

        notif = self.doCreate("obj_quest", message=message, target=target)
        return notif

    def answer_objQuest(self, message, parent):

        notif = self.doCreate("obj_quest_rep", message=message, parent=parent)
        return notif

    def share_object(self, target, url):

        notif = self.doCreate("share", target=target, url=url)
        return notif

    def regist_objAvailable(self, message, target):

        notif = self.doCreate("obj_regist_avail", message=message, target=target)

        target.registered_count += 1
        target.save()

        return notif

    def obj_available(self, target, message):

        #send sms
        pass
