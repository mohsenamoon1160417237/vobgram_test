from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from accounts.permissions.has_business_profile import HasBusinessProfile
from accounts.permissions.profile_first_step import ProfileFirstStep

from pre_order_service.models.pre_order_service import PreOrderService
from pre_order_service.model_serializers.pre_order_service import PreOrderServiceSerializer


class AddPreOrderService(GenericAPIView):

    permission_classes = [IsAuthenticated,ProfileFirstStep, HasBusinessProfile]

    def get(self, request, ord_id):

        pre_ord_serv = get_object_or_404(PreOrderService, id=ord_id)
        serializer = PreOrderServiceSerializer(pre_ord_serv)
        return Response({'status': 'get pre order service',
                         'service': serializer.data})

    def post(self, request):

        owner_id = request.user.business_profile.id

        serializer_data = request.data
        serializer_data['owner_id'] = owner_id

        serializer = PreOrderServiceSerializer(data=serializer_data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({'status': 'created pre order service',
                         'service': serializer.data})

    def put(self, request, ord_id):

        pre_ord_serv = get_object_or_404(PreOrderService, id=ord_id)
        owner_id = request.user.business_profile.id

        serializer_data = request.data
        serializer_data['owner_id'] = owner_id

        serializer = PreOrderServiceSerializer(pre_ord_serv, data=serializer_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'status': 'updated pre order service',
                         'service': serializer.data})

    def delete(self, request, ord_id):

        pre_ord_serv = get_object_or_404(PreOrderService, id=ord_id)

        pre_ord_serv.delete()

        return Response({'status': 'deleted pre order service'})
