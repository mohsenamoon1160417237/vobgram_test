from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.model_serializers.change_password import ChangePasswordSerializer



class ChangePassword(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        serializer_data = {
            'current_password': data['current_password'],
            'password': data['new_password']
        }

        serializer = ChangePasswordSerializer(request.user, data=serializer_data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'changed password'})
