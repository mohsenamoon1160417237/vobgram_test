from rest_framework.test import APITestCase

from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from .utils.create_admin_user import create_admin_user

from accounts.models.system_data_confirm import SystemDataConfirm
from business_service.models.valid_skill import ValidSkill


class TestValidSkill(APITestCase):

    skill_list_url = reverse('admin_valid_skills_list')
    accept_skill_url = reverse('admin_accept_valid_skill', kwargs={'skill_id': 1})
    reject_skill_url = reverse('admin_reject_valid_skill', kwargs={'skill_id': 1})

    def test_get_not_confirmed_valid_skill_list(self):

        user = create_admin_user()
        self.client.force_authenticate(user)
        response = self.client.get(self.skill_list_url)
        data = response.data
        assert data['status'] == 'get unconfirmed valid skills'

    def test_accept_valid_skill(self):

        user = create_admin_user()
        self.client.force_authenticate(user)
        skill = ValidSkill.objects.create(title='web')
        SystemDataConfirm.objects.create(target=skill)
        self.client.post(self.accept_skill_url)

        cnt = ContentType.objects.get_for_model(skill)

        admin_confirm = get_object_or_404(SystemDataConfirm,
                                          target_ct=cnt,
                                          target_id=1)

        confirmed = admin_confirm.is_confirmed
        assert confirmed is True

    def test_reject_valid_skill(self):

        user = create_admin_user()
        self.client.force_authenticate(user)
        skill = ValidSkill.objects.create(title='web')
        SystemDataConfirm.objects.create(target=skill)
        self.client.post(self.reject_skill_url)

        cnt = ContentType.objects.get_for_model(skill)

        admin_confirms = SystemDataConfirm.objects.filter(target_ct=cnt,
                                                          target_id=1)

        assert not admin_confirms.exists()

        skills = ValidSkill.objects.filter(id=1)
        assert not skills.exists()
