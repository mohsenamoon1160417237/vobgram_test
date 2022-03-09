from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.permissions.has_business_profile import HasBusinessProfile
from accounts.permissions.profile_first_step import ProfileFirstStep

from pre_order_service.models.pre_order_service import PreOrderService
from pre_order_service.model_serializers.pre_order_service import PreOrderServiceSerializer


class OwnerPreOrderServiceList(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasBusinessProfile]

    def get(self, request):

        services = PreOrderService.objects.filter(owner=request.user.business_profile)

        serializer = PreOrderServiceSerializer(services, many=True)

        return Response({'status': 'get own pre order services',
                         'services': serializer.data})
