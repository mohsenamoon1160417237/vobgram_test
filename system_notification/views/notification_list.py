from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from system_notification.model_serializers.notifications import SystemNotificationSerializer
from system_notification.models.system_notification import SystemNotification


class NotificationList(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        notifications = SystemNotification.objects.filter(receiver=request.user)

        serializer = SystemNotificationSerializer(notifications, many=True)

        return Response({'status': 'get notifications list',
                         'notifications': serializer.data})
