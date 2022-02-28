from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from accounts.permissions.profile_first_step import ProfileFirstStep

from business_service.models.service_request import ServiceRequest
from accounts.models.profiles.business import BusinessProfile
from accounts.models.system_data_confirm import SystemDataConfirm


class CustomerSendServiceRequest(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def post(self, request, prof_id, serv_id):

        profile = get_object_or_404(BusinessProfile, id=prof_id)

        service = get_object_or_404(ServiceRequest, id=serv_id)

        cnt = ContentType.objects.get_for_model(service)
        admin_conf = get_object_or_404(SystemDataConfirm,
                                       target_ct=cnt,
                                       target_id=service.id)

        if admin_conf.is_confirmed is False:

            if admin_conf.admin_profile is None:

                raise serializers.ValidationError({'error': 'You must wait for the admin to confirm the request'})

            else:

                raise serializers.ValidationError({'error': 'The request has been rejected by admin'})

        service.receivers.add(profile)

        service.save()

        return Response({'status': 'sent service request'})
