from system_notification.models.system_notification import SystemNotification


def create_systemNotif(receiver, msg, cnt, id, data_type):

    notification = SystemNotification.objects.create(receiver=receiver,
                                                     message=msg,
                                                     target_ct=cnt,
                                                     target_id=id,
                                                     data_type=data_type)

    return notification
