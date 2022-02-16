from rest_framework.test import APITestCase

from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from .utils.create_admin_user import create_admin_user
from business_service.tests.utils.create_business_profile import create_business_profile

from business_service.models.business_product import BusinessProduct
from accounts.models.admin_data_confirm import AdminDataConfirm


class TestProduct(APITestCase):

    accept_product_url = reverse('admin_accept_product', kwargs={'prod_id': 1})
    reject_product_url = reverse('admin_reject_product', kwargs={'prod_id': 1})

    def test_accept_product(self):

        user = create_admin_user()
        profile = create_business_profile(user)
        self.client.force_authenticate(user)

        product = BusinessProduct.objects.create(business_profile=profile,
                                                 title='app',
                                                 description='...')

        AdminDataConfirm.objects.create(target=product)

        post_data = {'comment': 'accepted'}

        response = self.client.post(self.accept_product_url, post_data)

        cnt = ContentType.objects.get_for_model(product)

        admin_confirm = get_object_or_404(AdminDataConfirm,
                                          target_ct=cnt,
                                          target_id=product.id)

        assert admin_confirm.is_confirmed is True

    def test_reject_product(self):

        user = create_admin_user()
        profile = create_business_profile(user)
        self.client.force_authenticate(user)

        product = BusinessProduct.objects.create(business_profile=profile,
                                                 title='app',
                                                 description='...')

        AdminDataConfirm.objects.create(target=product)

        post_data = {'comment': 'rejected'}

        response = self.client.post(self.reject_product_url, post_data)

        cnt = ContentType.objects.get_for_model(product)

        admin_confirm = get_object_or_404(AdminDataConfirm,
                                          target_ct=cnt,
                                          target_id=product.id)

        assert admin_confirm.is_confirmed is False
