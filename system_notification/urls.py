from django.urls import path

from .views.notification_list import NotificationList


urlpatterns = [

    path('list/', NotificationList.as_view(), name='notif_list'),
]