from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.permissions.profile_first_step import ProfileFirstStep


class HomeView(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def get(self, request):

        response = Response()
        response.data = {'message': 'success'}
        return response
