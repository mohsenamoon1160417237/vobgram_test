from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from system_notification.models.system_notification import SystemNotification
from system_notification.utils.sys_notif_manager import SystemNotificationManager


class NotificationList(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        notif_mng = SystemNotificationManager(request.user)

        data = notif_mng.list_notifs()

        return Response({'status': 'get notifications list',
                         'notifications': data})
