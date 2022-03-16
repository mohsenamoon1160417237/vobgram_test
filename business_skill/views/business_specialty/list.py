from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_business_profile import HasBusinessProfile

from business_skill.models.business_specialty import BusinessSpecialty
from business_skill.model_serializers.business_specialty import BusinessSpecialtySerializer


class ServerBusinessSpecialtyList(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasBusinessProfile]

    def get(self, request):

        user = request.user

        specialties = BusinessSpecialty.objects.filter(user=user)

        serializer = BusinessSpecialtySerializer(specialties, many=True)

        return Response({'status': 'specialty list',
                         'specialties': serializer.data})
