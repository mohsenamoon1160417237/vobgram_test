from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from accounts.permissions.profile_first_step import ProfileFirstStep
from accounts.permissions.has_username import HasUsername

from service_contract.models.service_contract import ServiceContract

from business_skill.models.valid_skill import ValidSkill


class AddSkillToContract(GenericAPIView):

    permission_classes = [IsAuthenticated, ProfileFirstStep, HasUsername]

    def post(self, request, ctr_id, skill_ttl):

        valid_skill = get_object_or_404(ValidSkill,
                                        title=skill_ttl)

        contract = get_object_or_404(ServiceContract, id=ctr_id)

        contract.skill.add(valid_skill)

        contract.save()

        return Response({'status': 'added skill to contract'})

    def delete(self, request, ctr_id, skill_ttl):

        contract = get_object_or_404(ServiceContract, id=ctr_id)

        valid_skill = get_object_or_404(ValidSkill, title=skill_ttl)

        contract.skill.remove(valid_skill)

        contract.save()

        return Response({'status': 'removed skill from contract'})
