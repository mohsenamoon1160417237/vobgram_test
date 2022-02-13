from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.contrib.contenttypes.models import ContentType

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.models.profiles.business import BusinessProfile
from accounts.models.admin_data_confirm import AdminDataConfirm

from accounts.model_serializers.admin_data_confirm import AdminDataConfirmSerializer
from accounts.model_serializers.business_profile import BusinessProfileSerializer




class BusinessData(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep]

    def get(self, request):

        user = request.user
        business_profiles = BusinessProfile.objects.filter(user=user)
        if business_profiles.exists():
            business_profile = business_profiles[0]
            cnt = ContentType.objects.get_for_model(business_profile)
            admin_data_confirms = AdminDataConfirm.objects.filter(target_ct=cnt,
                                                                  target_id=business_profile.id,
                                                                  is_latest=True)
            business_profile_serializer = BusinessProfileSerializer(business_profile)
            admin_confirm_serializer = AdminDataConfirmSerializer(admin_data_confirms, many=True)

            data = {
                'business_profile': business_profile_serializer.data,
                'admin_data_confirms': admin_confirm_serializer.data,
                'status': 'has data'
            }

            return Response(data)
        else:
            return Response({'status': 'no data'})

    def post(self, request):

        data = request.data

        serializer_data = {
            'company_name': data['company_name'],
            'company_phone_number': data['company_phone_number'],
            'user_id': request.user.id,
            'bio': request.data['bio'],
            'status': None
        }

        business_profiles = BusinessProfile.objects.filter(user=request.user)
        if business_profiles.exists():
            business_profile = business_profiles[0]
            serializer = BusinessProfileSerializer(business_profile, data=serializer_data)
            status = 'updated business data'
        else:
            serializer = BusinessProfileSerializer(data=serializer_data)
            status = 'created business data'

        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer_data.pop('user_id')
        serializer_data['status'] = status
        return Response(serializer_data)
