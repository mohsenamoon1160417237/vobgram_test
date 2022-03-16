from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_business_profile import HasBusinessProfile

from business_skill.model_serializers.business_specialty import BusinessSpecialtySerializer

from business_skill.models.business_specialty import BusinessSpecialty
from accounts.models.system_data_confirm import SystemDataConfirm
from system_notification.models.system_notification import SystemNotification


class ServerAddBusinessSpecialty(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasBusinessProfile]

    def get(self, request, spec_id):

        specialty = get_object_or_404(BusinessSpecialty, id=spec_id)

        serializer = BusinessSpecialtySerializer(specialty)

        return Response({'status': 'get business specialty',
                         'specialty': serializer.data})

    def post(self, request):

        user = request.user

        serializer_data = request.data
        serializer_data['user_id'] = user.id

        serializer = BusinessSpecialtySerializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({'status': 'added business specialty',
                         'specialty': serializer.data})

    def put(self, request, spec_id):

        specialty = get_object_or_404(BusinessSpecialty, id=spec_id)

        user = request.user

        serializer_data = request.data
        serializer_data['user_id'] = user.id

        serializer = BusinessSpecialtySerializer(specialty, serializer_data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({'status': 'updated business specialty',
                         'specialty': serializer.data})

    def delete(self, request, spec_id):

        specialty = get_object_or_404(BusinessSpecialty, id=spec_id)

        cnt = ContentType.objects.get_for_model(specialty)

        admin_confirm = get_object_or_404(SystemDataConfirm,
                                          target_ct=cnt,
                                          target_id=specialty.id)

        admin_confirm.delete()

        notifications = SystemNotification.objects.filter(target_ct=cnt,
                                                          target_id=spec_id)
        if notifications.exists():

            notification = notifications[0]
            notification.target_id = None
            notification.save()

        specialty.delete()

        return Response({'status': 'deleted business specialty'})
