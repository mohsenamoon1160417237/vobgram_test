from rest_framework.test import APITestCase, APITransactionTestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404

from accounts.tests.utils.create_first_step import create_first_step
from .utils.create_business_profile import create_business_profile
from .utils.create_and_confirm_skill import create_and_confirm_skill

from business_service.models.business_product import BusinessProduct
from business_service.models.business_product_step import BusinessProductStep


class TestProductStep(APITransactionTestCase):

    create_product_url = reverse('add_business_product')
    add_product_step_url = reverse('add_business_product_step', kwargs={'prod_id': 1})
    edit_get_product_step_url = reverse('update_delete_get_business_product_step', kwargs={'prod_step_id': 1})

    def test_delete_product_step(self):

        user = create_first_step()
        self.client.force_authenticate(user)
        business_prof = create_business_profile(user)
        create_and_confirm_skill(business_prof)

        add_data = {'skill_title': 'web',
                    'title': 'chat app',
                    'description': '...'}

        self.client.post(self.create_product_url, add_data)
        self.client.post(self.create_product_url, add_data)

        post_data = {'note': '...',
                     'step_url': 'https://google.com',
                     'from_date': '2020-02-10',
                     'to_date': '2020-02-20'}

        self.client.post(self.add_product_step_url, post_data)

        response = self.client.delete(self.edit_get_product_step_url)
        data = response.data

        assert data['status'] == 'deleted product step'

        product = get_object_or_404(BusinessProduct, id=1)
        product_steps = BusinessProductStep.objects.filter(id=1)

        assert not product_steps.exists()
        assert product.max_step_number == 0
