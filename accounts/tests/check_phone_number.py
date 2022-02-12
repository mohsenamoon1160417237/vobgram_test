from rest_framework.test import APITestCase
from django.urls import reverse
from accounts.models.UserRegistration import UserRegistration


class TestCheckPhoneNumber(APITestCase):

    url = reverse('check_phone_number')

    def test_new_phone_number(self):

        test_data = {'phone_number': '9892342342'}
        response = self.client.post(self.url, test_data)
        data = response.data
        assert data['status'] == 'new user'
        users = UserRegistration.objects.filter(phone_number=test_data['phone_number'])
        assert users.exists()
        assert users.count() == 1

    def test_existing_phone_number(self):

        UserRegistration.objects.create(phone_number="12345678")
        test_data = {'phone_number': '12345678'}
        response = self.client.post(self.url, test_data)
        data = response.data
        assert data['phone_number'] == '12345678'
        assert data['status'] == 'registered'
