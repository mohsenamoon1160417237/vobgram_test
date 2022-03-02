from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError

from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_business_profile import HasBusinessProfile
from system_notification.utils.create_systemNotification import create_systemNotif

from business_service.models.service_request import ServiceRequest

from business_service.model_serializers.service_request_bid import ServiceRequestBidSerializer


class ServerServiceRequestBid(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasBusinessProfile]

    def post(self, request, serv_id):

        data = request.data

        service_request = get_object_or_404(ServiceRequest, id=serv_id)

        serializer_data = {'bidder_id': request.user.business_profile.id,
                           'service_request_id': serv_id,
                           'suggestion_text': data['suggestion_text'],
                           'price': data['price'],
                           'days': data['days']}

        serializer = ServiceRequestBidSerializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)

        if request.user.business_profile not in service_request.receivers.all():

            raise ValidationError({'error': 'You can not bid on this request'})

        if service_request.finished is True:

            raise ValidationError({'error': 'The request is closed'})

        bid = serializer.save()

        cnt = ContentType.objects.get_for_model(bid)

        first_name = request.user.personal_profile.first_name
        last_name = request.user.personal_profile.last_name

        create_systemNotif(service_request.requester.user,
                           '"{} {}" bid on your request'.format(first_name, last_name),
                           cnt,
                           bid.id,
                           None)

        return Response({'status': 'bid service request',
                         'bid': serializer.data})
        