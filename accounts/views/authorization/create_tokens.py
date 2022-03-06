from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from accounts.models.UserRegistration import UserRegistration
from accounts.models.profiles.customer import CustomerProfile

from accounts.model_serializers.register import RegisterSerializer

from accounts.views.utils.create_token import create_token




class CreateTokens(GenericAPIView):

    def post(self, request):

        password = request.data['password']
        phone_number = request.data['phone_number']
        user = get_object_or_404(UserRegistration, phone_number=phone_number)

        if user.registered is True:
            if user.check_password(password):
                data = create_token(user)
                data['status'] = 'logged in'
                return Response(data)
            else:
                return Response({'status': 'wrong password'})

        else:
            serializer = RegisterSerializer(user, data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            if request.data['user_type'] == 'customer':

                CustomerProfile.objects.create(user=user)

            data = create_token(user)
            data['status'] = 'registered and logged in'
            return Response(data)
