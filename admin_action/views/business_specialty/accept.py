from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from admin_action.permissions.is_admin import IsAdmin
from system_notification.utils.create_systemNotification import create_systemNotif
from admin_action.views.utils.admin_accept_or_reject import admin_accept_or_reject

from business_service.models.business_specialty import BusinessSpecialty


class AdminBusinessSpecialtyAccept(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, spec_id):

        admin_profile = request.user.admin_profile

        specialty = get_object_or_404(BusinessSpecialty, id=spec_id)

        cnt = ContentType.objects.get_for_model(specialty)

        admin_accept_or_reject(True, None, admin_profile, cnt, specialty.id, request.data['comment'])

        create_systemNotif(specialty.user,
                           'Your specialty "{}" has been confirmed by admin'.format(specialty.title),
                           specialty,
                           None)

        return Response({'status': 'accepted specialty'})
