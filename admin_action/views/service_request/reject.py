from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from admin_action.permissions.is_admin import IsAdmin

from admin_action.views.utils.admin_accept_or_reject import admin_accept_or_reject

from business_service.models.service_request import ServiceRequest



class AdminRejectServiceRequest(GenericAPIView):

    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, req_id):

        admin_profile = request.user.admin_profile

        service_request = get_object_or_404(ServiceRequest, id=req_id)

        cnt = ContentType.objects.get_for_model(service_request)

        admin_accept_or_reject(False, None, admin_profile, cnt, service_request.id, request.data['comment'])

        return Response({'status': 'rejected service request'})
