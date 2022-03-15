from django.urls import path

from .views.notification_list import NotificationList
from .views.unseen_count import UnseenNotificationCount


urlpatterns = [

    path('list/', NotificationList.as_view(), name='notif_list'),
    path('unseen_count/', UnseenNotificationCount.as_view(), 'unseen_notif_count'),
]
