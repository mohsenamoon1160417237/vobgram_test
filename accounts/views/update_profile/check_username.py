from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models.profiles.personal import PersonalProfile


class CheckUsernamevalidity(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, query):

        profiles = PersonalProfile.objects.filter(username=query)

        if profiles.exists():

            return Response({'status': 'duplicate username'})

        return Response({'status': 'success'})
