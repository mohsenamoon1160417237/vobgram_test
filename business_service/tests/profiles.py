from rest_framework.test import APITestCase, APITransactionTestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from accounts.tests.utils.create_first_step import create_first_step
from accounts.models.system_data_confirm import SystemDataConfirm
from accounts.models.profiles.business import BusinessProfile

from business_service.models.business_skill import BusinessSkill
from business_service.models.valid_skill import ValidSkill



class TestProfiles(APITransactionTestCase):

    search_profiles_url = reverse('search_business_profile', kwargs={'query': 'dev'})
    add_valid_skill_url = reverse('add_valid_skill')
    choose_skill_url = reverse('choose_skill')
    business_data_url = reverse('update_business_data')
    view_profile_url = reverse('view_profile', kwargs={'id': 1})


    def test_search_business_no_profiles(self):

        user = create_first_step()
        self.client.force_authenticate(user)
        response = self.client.get(self.search_profiles_url)
        data = response.data
        assert data['status'] == 'no profiles'

    def test_search_business_found_profiles(self):

        user = create_first_step()
        self.client.force_authenticate(user)

        business_data = {'company_name': 'mohsen',
                         'company_phone_number': '123123',
                         'bio': 'hello'}

        self.client.post(self.business_data_url, business_data)

        add_skill_data = {'title': 'web',
                          'description': 'web development'}
        self.client.post(self.add_valid_skill_url, add_skill_data)

        valid_skill = get_object_or_404(ValidSkill,
                                        title='web')

        cnt = ContentType.objects.get_for_model(valid_skill)
        admin_confirm = get_object_or_404(SystemDataConfirm,
                                          target_ct=cnt,
                                          target_id=valid_skill.id)

        admin_confirm.is_confirmed = True
        admin_confirm.save()

        business_profile = get_object_or_404(BusinessProfile,
                                             company_name='mohsen',
                                             company_phone_number='123123',
                                             user=user)

        cnt = ContentType.objects.get_for_model(business_profile)
        company_name_admin = get_object_or_404(SystemDataConfirm,
                                               target_ct=cnt,
                                               target_id=business_profile.id,
                                               data_type='company_name')
        company_name_admin.is_confirmed = True
        company_name_admin.save()
        company_phone_number_admin = get_object_or_404(SystemDataConfirm,
                                                       target_ct=cnt,
                                                       target_id=business_profile.id,
                                                       data_type='company_phone_number')
        company_phone_number_admin.is_confirmed = True
        company_phone_number_admin.save()

        choose_skill_data = {'title': 'web',
                             'comment': '3 years'}

        self.client.post(self.choose_skill_url, choose_skill_data)

        skill = get_object_or_404(BusinessSkill,
                                  business_profile=business_profile)
        skill.score = 4
        skill.save()

        response = self.client.get(self.search_profiles_url)
        data = response.data
        assert data['status'] == 'profiles'
        assert data['profiles'] is not None

    def test_view_profile(self):

        user = create_first_step()
        self.client.force_authenticate(user)

        business_data = {'company_name': 'mohsen',
                         'company_phone_number': '123123',
                         'bio': 'hello'}

        self.client.post(self.business_data_url, business_data)

        response = self.client.get(self.view_profile_url)
        data = response.data
        assert data['status'] == 'private profile'
