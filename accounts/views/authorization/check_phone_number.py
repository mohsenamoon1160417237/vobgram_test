from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from accounts.models.UserRegistration import UserRegistration



class CheckPhoneNumber(GenericAPIView):

    def post(self, request):

        phone_number = request.data['phone_number']
        users = UserRegistration.objects.filter(phone_number=phone_number)
        if users.exists():
            return Response({'phone_number': phone_number,
                             'status': 'registered'})
        else:
            # send sms
            UserRegistration.objects.create(phone_number=phone_number)
            return Response({'status': 'new user'})
