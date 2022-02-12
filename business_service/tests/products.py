from rest_framework.test import APITransactionTestCase
from django.urls import reverse

from .utils.create_business_profile import create_business_profile
from accounts.tests.utils.create_first_step import create_first_step



class TestProducts(APITransactionTestCase):

    get_create_product_url = reverse('add_get_business_product')

    def test_get_products(self):

        user = create_first_step()
        self.client.force_authenticate(user)
        create_business_profile(user)
        response = self.client.get(self.get_create_product_url)
        data = response.data
        assert data['status'] == 'get business products'

    def test_create_product(self):

        user = create_first_step()
        self.client.force_authenticate(user)
        create_business_profile(user)

        add_data = {'skill_title': 'web'}
