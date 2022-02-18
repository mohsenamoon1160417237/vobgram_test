from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep

from business_service.models.service_request import ServiceRequest
from accounts.models.profiles.business import BusinessProfile


class CustomerSendServiceRequest(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def post(self, request, prof_id, serv_id):

        profile = get_object_or_404(BusinessProfile, id=prof_id)

        service = get_object_or_404(ServiceRequest, id=serv_id)

        service.receivers.add(profile)

        service.save()

        return Response({'status': 'sent service request'})
