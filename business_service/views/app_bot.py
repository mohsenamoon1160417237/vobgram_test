from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from business_service.model_serializers.app_bot import AppBotSz
from business_service.models.app_bot import AppBot

from accounts.permissions.has_business_profile import HasBusinessProfile
from accounts.permissions.profile_first_step import ProfileFirstStep


class AppBotView(GenericAPIView):

    permission_classes = [IsAuthenticated,
                          HasBusinessProfile,
                          ProfileFirstStep]

    def get(self, request, bot_id):

        bot = get_object_or_404(AppBot,
                                id=bot_id)
        sz = AppBotSz(bot)
        return Response({'status': 'get app bot',
                         'bot': sz.data})

    def post(self, request):

        sz_data = request.data

        serv_cntr_id = request.data['service_contract_id']

        sz_data.update(service_contract_id=serv_cntr_id)

        sz_data.update(business_profile_id=request.user.business_profile.id)

        sz = AppBotSz(data=sz_data)
        sz.is_valid(raise_exception=True)
        sz.save()

        return Response({'status': 'created app bot',
                         'bot': sz.data})

    def put(self, request, bot_id):

        bot = get_object_or_404(AppBot,
                                id=bot_id)

        sz_data = request.data

        serv_cntr_id = request.data['service_contract_id']

        if serv_cntr_id is not None:
            sz_data.update(service_contract_id=serv_cntr_id)
        else:
            sz_data.update(service_contract_id=None)

        sz_data.update(business_profile_id=request.user.business_profile.id)

        sz = AppBotSz(data=sz_data, instance=bot)
        sz.is_valid(raise_exception=True)
        sz.save()

        return Response({'status': 'updated app bot',
                         'bot': sz.data})

    def delete(self, request, bot_id):

        bot = get_object_or_404(AppBot,
                                id=bot_id)

        bot.delete()

        return Response({'status': 'deleted app bot'})
