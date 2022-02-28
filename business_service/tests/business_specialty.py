from rest_framework.test import APITestCase

from django.urls import reverse

from accounts.tests.utils.create_first_step import create_first_step
from .utils.create_business_profile import create_business_profile

from business_service.models.business_specialty import BusinessSpecialty
from accounts.models.system_data_confirm import SystemDataConfirm


class TestBusinessSpecialty(APITestCase):

    add_specialty_url = reverse('add_business_specialty')
    edit_specialty_url = reverse('edit_get_business_specialty', kwargs={'spec_id': 1})

    def test_create_business_specialty(self):

        user = create_first_step()
        create_business_profile(user)
        self.client.force_authenticate(user)

        post_data = {
            'title': 'math',
            'note': 'master at math',
            'education_institute_name': 'some where'
        }

        self.client.post(self.add_specialty_url, post_data)

        specialties = BusinessSpecialty.objects.filter(business_profile=user.business_profile,
                                                       title='math')

        assert specialties.exists()

    def test_delete_business_specialty(self):

        user = create_first_step()
        create_business_profile(user)
        self.client.force_authenticate(user)

        specialty = BusinessSpecialty.objects.create(business_profile=user.business_profile,
                                                     title='math',
                                                     note='...',
                                                     education_institute_name='...')
        SystemDataConfirm.objects.create(target=specialty)

        self.client.delete(self.edit_specialty_url)

        specialties = BusinessSpecialty.objects.filter(id=specialty.id)

        assert not specialties.exists()
