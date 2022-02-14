from rest_framework.test import APITestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404

from .utils.create_business_profile import create_business_profile
from .utils.create_and_confirm_skill import create_and_confirm_skill
from accounts.tests.utils.create_first_step import create_first_step

from business_service.models.business_product import BusinessProduct
from business_service.models.business_product_step import BusinessProductStep



class TestProducts(APITestCase):

    get_create_product_url = reverse('add_get_business_product')
    update_delete_product_url = reverse('update_delete_business_product', kwargs={'prod_id': 1})
    add_product_step_url = reverse('add_business_product_step', kwargs={'prod_id': 1})
    edit_product_step_url = reverse('edit_business_product_step', kwargs={'prod_id': 1,
                                                                          'prod_step_id': 1})

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
        business_prof = create_business_profile(user)
        create_and_confirm_skill(business_prof)

        add_data = {'skill_title': 'web',
                    'title': 'chat app',
                    'description': '...'}

        response = self.client.post(self.get_create_product_url, add_data)
        data = response.data
        assert data['status'] == 'created product'
        assert data['product'] is not None

    def test_delete_product(self):

        user = create_first_step()
        self.client.force_authenticate(user)
        business_prof = create_business_profile(user)
        skill = create_and_confirm_skill(business_prof)

        add_data = {'skill_title': 'web',
                    'title': 'chat app',
                    'description': '...'}

        self.client.post(self.get_create_product_url, add_data)

        response = self.client.delete(self.update_delete_product_url)
        data = response.data
        assert data['status'] == 'deleted product'

        business_products = BusinessProduct.objects.filter(business_profile=business_prof,
                                                           business_skill=skill,
                                                           title='chat app')

        assert not business_products.exists()

    def test_update_product(self):

        user = create_first_step()
        self.client.force_authenticate(user)
        business_prof = create_business_profile(user)
        skill = create_and_confirm_skill(business_prof)

        add_data = {'skill_title': 'web',
                    'title': 'chat app',
                    'description': '...'}

        self.client.post(self.get_create_product_url, add_data)

        product = get_object_or_404(BusinessProduct,
                                    business_profile=business_prof,
                                    business_skill=skill,
                                    title='chat app')

        put_data = {'skill_title': 'web',
                    'title': 'blog app',
                    'description': '...'}

        response = self.client.put(self.update_delete_product_url, put_data)
        data = response.data

        assert data['status'] == 'updated product'

        products = BusinessProduct.objects.filter(business_profile=business_prof,
                                                  business_skill=skill,
                                                  title='blog app')

        assert products.exists()

    def add_business_product_step(self):

        user = create_first_step()
        self.client.force_authenticate(user)
        business_prof = create_business_profile(user)
        skill = create_and_confirm_skill(business_prof)

        add_data = {'skill_title': 'web',
                    'title': 'chat app',
                    'description': '...'}

        self.client.post(self.get_create_product_url, add_data)

        business_product = get_object_or_404(BusinessProduct,
                                             business_profile=business_prof,
                                             business_skill=skill,
                                             title='chat app')

        post_data = {'note': '...',
                     'step_url': 'https://google.com',
                     'from_date': '2020-02-10',
                     'to_date': '2020-02-20'}

        response = self.client.post(self.add_product_step_url, post_data)
        data = response.data
        assert data['status'] == 'created business product step'

        product_steps = BusinessProductStep.objects.filter(business_product=business_product,
                                                           note='...')

        assert product_steps.exists()

    def test_delete_product_step(self):

        user = create_first_step()
        self.client.force_authenticate(user)
        business_prof = create_business_profile(user)
        create_and_confirm_skill(business_prof)

        add_data = {'skill_title': 'web',
                    'title': 'chat app',
                    'description': '...'}

        self.client.post(self.get_create_product_url, add_data)

        post_data = {'note': '...',
                     'step_url': 'https://google.com',
                     'from_date': '2020-02-10',
                     'to_date': '2020-02-20'}

        self.client.post(self.add_product_step_url, post_data)

        response = self.client.delete(self.edit_product_step_url)
        data = response.data

        assert data['status'] == 'deleted product step'

        product = get_object_or_404(BusinessProduct, id=1)
        product_steps = BusinessProductStep.objects.filter(id=1)

        assert not product_steps.exists()
        assert product.max_step_number == 0