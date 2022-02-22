from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_business_profile import HasBusinessProfile


from business_service.model_serializers.view.business_specialty import BusinessSpecialtyViewSerializer

from business_service.models.business_specialty import BusinessSpecialty


class ServerBusinessSpecialtyList(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasBusinessProfile]


    def get(self, request):

        user = request.user
        business_profile = user.business_profile

        specialties = BusinessSpecialty.objects.filter(business_profile=business_profile)

        serializer = BusinessSpecialtyViewSerializer(specialties, many=True)

        return Response({'status': 'specialty list',
                         'specialties': serializer.data})
