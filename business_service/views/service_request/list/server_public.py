from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_business_profile import HasBusinessProfile

from accounts.models.system_data_confirm import SystemDataConfirm
from business_skill.models.business_skill import BusinessSkill
from business_service.models.service_request import ServiceRequest

from business_service.model_serializers.view.service_request.customer import CustomerServiceRequestViewSerializer

class ServerPublicServiceRequestList(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasBusinessProfile]

    def get(self, request):

        business_profile = request.user.business_profile

        skills = BusinessSkill.objects.filter(business_profile=business_profile,
                                              score__gt=0)

        valid_skills = skills.values('valid_skill')

        request_cnt = ContentType.objects.get(app_label='business_service',
                                              model='servicerequest')

        request_admin_confs = SystemDataConfirm.objects.filter(target_ct=request_cnt,
                                                               is_latest=True,
                                                               is_confirmed=True)

        requests = ServiceRequest.objects.filter(skill__in=valid_skills,
                                                 request_type='public',
                                                 id__in=request_admin_confs.values('target_id'),
                                                 finished=False)

        serializer = CustomerServiceRequestViewSerializer(requests, many=True)

        return Response({'status': 'get service requests',
                         'service requests': serializer.data})
