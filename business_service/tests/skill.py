from rest_framework.test import APITestCase, APITransactionTestCase

from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from accounts.tests.utils.create_first_step import create_first_step

from business_skill.models.valid_skill import ValidSkill
from business_skill.models.business_skill import BusinessSkill
from accounts.models.system_data_confirm import SystemDataConfirm



class TestSkill(APITransactionTestCase):

    search_skill_url1 = reverse('search_valid_skill', kwargs={'query': 'web'})
    search_skill_url2 = reverse('search_valid_skill', kwargs={'query': 'x'})
    add_skill_url = reverse('add_valid_skill')
    choose_skill_url = reverse('choose_skill')
    business_profile_url = reverse('update_business_data')

    def create_confirmed_skill(self):

        skill = ValidSkill.objects.create(title='web',
                                          description='web development')
        admin_confirm = SystemDataConfirm.objects.create(target=skill,
                                                         is_confirmed=True)
        return skill

    def test_search_skill_at_least_one_result(self):

        self.create_confirmed_skill()
        user = create_first_step()
        self.client.force_authenticate(user)
        response = self.client.get(self.search_skill_url1)
        data = response.data
        assert data['status'] == 'found skills'
        assert data['skills'][0]['title'] == 'web'
        assert data['skills'][0]['description'] == 'web development'

    def test_search_skill_no_result(self):

        user = create_first_step()
        self.client.force_authenticate(user)
        response = self.client.get(self.search_skill_url2)
        data = response.data
        assert data['status'] == 'no skills found'
        assert len(data['skills']) == 0

    def test_add_valid_skill(self):

        user = create_first_step()
        self.client.force_authenticate(user)

        post_data = {"company_name": "mohsen",
                     "company_phone_number": "2342342",
                     "bio": "hello"}
        self.client.post(self.business_profile_url, post_data)

        post_data = {'title': 'web',
                     'description': 'web development'}
        response = self.client.post(self.add_skill_url, post_data)
        data = response.data
        assert data['status'] == 'added new skill'
        valid_skills = ValidSkill.objects.filter(title='web')
        assert valid_skills.exists()
        assert valid_skills.count() == 1
        valid_skill = valid_skills[0]
        assert valid_skill.title == 'web'
        assert valid_skill.description == 'web development'

        cnt = ContentType.objects.get_for_model(valid_skill)

        admin_confirms = SystemDataConfirm.objects.filter(target_ct=cnt,
                                                          target_id=valid_skill.id)
        assert admin_confirms.exists()
        assert admin_confirms.count() == 1

    def test_choose_skill(self):

        user = create_first_step()
        self.client.force_authenticate(user)

        post_data = {"company_name": "mohsen",
                     "company_phone_number": "2342342",
                     "bio": "hello"}
        self.client.post(self.business_profile_url, post_data)

        valid_skill = ValidSkill.objects.create(title='web',
                                                description='web development')

        admin_confirm = SystemDataConfirm.objects.create(target=valid_skill,
                                                         is_confirmed=True)

        post_data = {'title': 'web'}
        response = self.client.post(self.choose_skill_url, post_data)
        data = response.data

        valid_skill = get_object_or_404(ValidSkill, title='web')

        assert data['status'] == 'choosed skill'
        assert data['skill'] is not None
        assert valid_skill.selected_number == 1

    def test_remove_business_skill_(self):

        user = create_first_step()
        self.client.force_authenticate(user)
        post_data = {"company_name": "mohsen",
                     "company_phone_number": "2342342",
                     "bio": "hello"}
        self.client.post(self.business_profile_url, post_data)

        post_data = {'title': 'web',
                     'description': 'web development'}
        self.client.post(self.add_skill_url, post_data)

        valid_Skill = get_object_or_404(ValidSkill,
                                        title='web')

        cnt =  ContentType.objects.get_for_model(valid_Skill)

        admin_confirm = get_object_or_404(SystemDataConfirm,
                                          target_ct=cnt,
                                          target_id=valid_Skill.id)

        admin_confirm.is_confirmed = True
        admin_confirm.save()

        post_data = {'title': 'web'}
        self.client.post(self.choose_skill_url, post_data)

        delete_data = {'title': 'web'}
        response = self.client.delete(self.choose_skill_url, delete_data)
        data = response.data
        assert data['status'] == 'removed skill'

        valid_skill = get_object_or_404(ValidSkill, title='web')

        business_skills = BusinessSkill.objects.filter(business_profile=user.business_profile,
                                                       valid_skill=valid_skill)

        assert not business_skills.exists()
        assert business_skills.count() == 0
