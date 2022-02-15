from rest_framework.test import APITestCase

from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from .utils.create_admin_user import create_admin_user

from accounts.models.profiles.business import BusinessProfile
from accounts.models.admin_data_confirm import AdminDataConfirm


class TestBusinessData(APITestCase):

    accept_business_data_url = reverse('admin_accept_business_data', kwargs={'prof_id': 1,
                                                                             'data_type': 'company_name'})
    reject_business_data_url = reverse('admin_reject_business_data', kwargs={'prof_id': 1,
                                                                             'data_type': 'company_name'})

    def test_accept_business_data(self):

        user = create_admin_user()
        self.client.force_authenticate(user)
        profile = BusinessProfile.objects.create(user=user,
                                                 company_name='mohsen',
                                                 company_phone_number='123123',
                                                 bio='hello')

        cnt = ContentType.objects.get_for_model(profile)

        AdminDataConfirm.objects.create(target=profile,
                                        data_type='company_name')

        post_data = {'comment': 'hello'}

        response = self.client.post(self.accept_business_data_url, post_data)
        data = response.data

        assert data['status'] == 'accepted business data'

        cmp_name_conf = get_object_or_404(AdminDataConfirm,
                                          target_ct=cnt,
                                          target_id=profile.id,
                                          data_type='company_name')

        assert cmp_name_conf.is_confirmed is True

    def test_reject_business_data(self):

        user = create_admin_user()
        self.client.force_authenticate(user)
        profile = BusinessProfile.objects.create(user=user,
                                                 company_name='mohsen',
                                                 company_phone_number='123123',
                                                 bio='hello')

        cnt = ContentType.objects.get_for_model(profile)

        AdminDataConfirm.objects.create(target=profile,
                                        data_type='company_name')

        post_data = {'comment': 'hello'}

        response = self.client.post(self.reject_business_data_url, post_data)
        data = response.data

        assert data['status'] == 'rejected business data'

        cmp_name_conf = get_object_or_404(AdminDataConfirm,
                                          target_ct=cnt,
                                          target_id=profile.id,
                                          data_type='company_name')

        assert cmp_name_conf.is_confirmed is False
