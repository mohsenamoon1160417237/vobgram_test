from rest_framework.test import APITestCase
from django.urls import reverse
from accounts.models.UserRegistration import UserRegistration


class TestCreateTokens(APITestCase):

    url = reverse('create_tokens')

    def create_user(self):

        user = UserRegistration.objects.create(phone_number='12345678')
        user.set_password('mohsen1160417237')
        user.save()
        return user

    def test_registered_user_true_password(self):

        user = self.create_user()
        user.registered = True
        user.save()
        test_data = {'phone_number': '12345678',
                     'password': 'mohsen1160417237',
                     'user_type': 'server'}

        response = self.client.post(self.url, test_data)
        data = response.data
        assert data['status'] == 'logged in'
        assert data['access'] is not None
        assert data['refresh'] is not None

    def test_registered_user_false_password(self):

        user = self.create_user()
        user.registered = True
        user.save()
        test_data = {'phone_number': '12345678',
                     'password': 'mohsen1160417236',
                     'user_type': 'normal'}
        response = self.client.post(self.url, test_data)
        data = response.data
        assert data['status'] == 'wrong password'

    def test_unregistered_user(self):

        UserRegistration.objects.create(phone_number='12345678')
        test_data = {'phone_number': '12345678',
                     'password': 'mohsen1160417237',
                     'user_type': 'normal'}
        response = self.client.post(self.url, test_data)
        data = response.data
        assert data['status'] == 'registered and logged in'
        assert data['access'] is not None
        assert data['refresh'] is not None
        users = UserRegistration.objects.filter(phone_number='12345678')
        assert users.exists()
        assert users.count() == 1
        user = users[0]
        assert user.check_password('mohsen1160417237')
