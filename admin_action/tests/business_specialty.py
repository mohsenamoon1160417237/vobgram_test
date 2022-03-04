from rest_framework.test import APITestCase
from django.urls import reverse

from django.shortcuts import get_object_or_404

from .utils.create_admin_user import create_admin_user

from business_skill.models.business_specialty import BusinessSpecialty
from accounts.models.system_data_confirm import SystemDataConfirm
from accounts.models.profiles.business import BusinessProfile


class TestBusinessSpecialty(APITestCase):

    accept_specialty_url = reverse('admin_accept_business_specialty', kwargs={'spec_id': 1})
    reject_specialty_url = reverse('admin_reject_business_specialty', kwargs={'spec_id': 1})

    def test_accept_specialty(self):

        user = create_admin_user()
        profile = BusinessProfile.objects.create(user=user,
                                                 company_name='x',
                                                 company_phone_number=123,
                                                 bio='hello')
        self.client.force_authenticate(user)

        specialty = BusinessSpecialty.objects.create(business_profile=profile,
                                                     title='math',
                                                     note='good',
                                                     education_institute_name='uni')

        admin_conf = SystemDataConfirm.objects.create(target=specialty)

        post_data = {'comment': 'good'}

        self.client.post(self.accept_specialty_url, post_data)

        admin_conf = get_object_or_404(SystemDataConfirm, id=admin_conf.id)

        assert admin_conf.is_confirmed is True

    def test_accept_business_specialty(self):

        user = create_admin_user()
        profile = BusinessProfile.objects.create(user=user,
                                                 company_name='x',
                                                 company_phone_number=123,
                                                 bio='hello')
        self.client.force_authenticate(user)

        specialty = BusinessSpecialty.objects.create(business_profile=profile,
                                                     title='math',
                                                     note='good',
                                                     education_institute_name='uni')

        admin_conf = SystemDataConfirm.objects.create(target=specialty)

        post_data = {'comment': 'good'}

        self.client.post(self.reject_specialty_url, post_data)

        admin_conf = get_object_or_404(SystemDataConfirm, id=admin_conf.id)

        assert admin_conf.is_confirmed is False
