from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from system_notification.utils.sys_notif_manager import SystemNotificationManager
from system_notification.models.system_notification import SystemNotification


class UnseenNotificationCount(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        notif_mng = SystemNotificationManager(request.user)

        count = notif_mng.count_unseenNotifs()

        return Response({'status': 'get unseen notifications count',
                         'count': count})
