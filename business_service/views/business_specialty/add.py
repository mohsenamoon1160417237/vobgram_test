from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_business_profile import HasBusinessProfile

from business_service.model_serializers.business_specialty import BusinessSpecialtySerializer
from business_service.model_serializers.view.business_specialty import BusinessSpecialtyViewSerializer

from business_service.models.business_specialty import BusinessSpecialty
from accounts.models.admin_data_confirm import AdminDataConfirm


class ServerAddBusinessSpecialty(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasBusinessProfile]

    def get(self, request, spec_id):

        specialty = get_object_or_404(BusinessSpecialty, id=spec_id)

        serializer = BusinessSpecialtyViewSerializer(specialty)

        return Response({'status': 'get business specialty',
                         'specialty': serializer.data})

    def post(self, request):

        user = request.user
        business_profile = user.business_profile

        serializer_data = {
            'business_profile_id': business_profile.id,
            'title': request.data['title'],
            'note': request.data['note'],
            'education_institute_name': request.data['education_institute_name']
        }

        serializer = BusinessSpecialtySerializer(data=serializer_data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({'status': 'added business specialty',
                         'specialty': serializer.data})

    def put(self, request, spec_id):

        specialty = get_object_or_404(BusinessSpecialty, id=spec_id)

        user = request.user
        business_profile = user.business_profile

        serializer_data = {
            'business_profile_id': business_profile.id,
            'title': request.data['title'],
            'note': request.data['note'],
            'education_institute_name': request.data['education_institute_name']
        }

        serializer = BusinessSpecialtySerializer(specialty, serializer_data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({'status': 'updated business specialty',
                         'specialty': serializer.data})

    def delete(self, request, spec_id):

        specialty = get_object_or_404(BusinessSpecialty, id=spec_id)

        cnt = ContentType.objects.get_for_model(specialty)

        admin_confirm = get_object_or_404(AdminDataConfirm,
                                          target_ct=cnt,
                                          target_id=specialty.id)

        admin_confirm.delete()
        specialty.delete()

        return Response({'status': 'deleted business specialty'})
