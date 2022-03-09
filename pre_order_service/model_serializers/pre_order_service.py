from rest_framework import serializers
from django.shortcuts import get_object_or_404

from pre_order_service.models.pre_order_service import PreOrderService
from accounts.models.profiles.business import BusinessProfile

from accounts.model_serializers.utils.create_admin_data_confirm import create_admin_data_confirm
from accounts.model_serializers.view.public_user_register import PublicUserRegisterViewSerializer
from admin_action.views.utils.check_system_confirm_latest import check_system_confirm_latest


class PreOrderServiceSerializer(serializers.ModelSerializer):

    owner_id = serializers.IntegerField()
    users = serializers.SerializerMethodField()

    class Meta:

        model = PreOrderService
        fields = ['owner_id',
                  'title',
                  'description',
                  'total_price',
                  'off_amount',
                  'off_price',
                  'users',
                  'id']

        read_only_fields = ['off_price',
                            'users',
                            'id']

        write_only_fields = ['owner_id']

    def get_users(self, obj):

        users = obj.user_register.all()
        serializer = PublicUserRegisterViewSerializer(users, many=True)
        return serializer.data

    def create(self, validated_data):

        owner = get_object_or_404(BusinessProfile, id=validated_data['owner_id'])

        service = PreOrderService.objects.create(owner=owner,
                                                 title=validated_data['title'],
                                                 description=validated_data['description'],
                                                 total_price=validated_data['total_price'],
                                                 off_amount=validated_data['off_amount'])

        off_price = validated_data['total_price'] - validated_data['off_amount']

        service.off_price = off_price
        service.save()

        create_admin_data_confirm(service, owner, None)

        return service

    def update(self, instance, validated_data):

        instance.title = validated_data['title']
        instance.description = validated_data['description']
        instance.total_price = validated_data['total_price']
        instance.off_amount = validated_data['off_amount']
        off_price = validated_data['total_price'] - validated_data['off_amount']

        instance.off_price = off_price

        instance.save()

        owner = get_object_or_404(BusinessProfile, id=validated_data['owner_id'])

        check_system_confirm_latest(instance, owner, None)

        return instance
