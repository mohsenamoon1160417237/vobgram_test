from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from accounts.model_serializers.first_step import ProfileFirstStepSerializer
from accounts.models.profiles.personal import PersonalProfile


class UpdateProfileFirstStep(GenericAPIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user
        profiles = PersonalProfile.objects.filter(user=user)
        if profiles.exists():
            profile = profiles[0]
            serializer = ProfileFirstStepSerializer(profile)
            return Response({'profile': serializer.data,
                             'status': 'found profile'})
        return Response({'status': 'no profile'})

    def post(self, request):

        user_id = request.user.id

        serializer_data = request.data
        serializer_data['user_id'] = user_id

        profiles = PersonalProfile.objects.filter(user__id=user_id)

        if profiles.exists():
            profile = profiles[0]
            serializer = ProfileFirstStepSerializer(profile, data=serializer_data)
        else:
            serializer = ProfileFirstStepSerializer(data=serializer_data)

        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=user_id)
        response = Response({'status': 'created profile',
                             'profile': serializer.data})
        return response
