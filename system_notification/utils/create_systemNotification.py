from system_notification.models.system_notification import SystemNotification


def create_systemNotif(receiver, msg, target, data_type):

    notification = SystemNotification.objects.create(receiver=receiver,
                                                     message=msg,
                                                     target=target,
                                                     data_type=data_type)

    return notification
