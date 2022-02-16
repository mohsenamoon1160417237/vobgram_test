from rest_framework.test import APITestCase

from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from .utils.create_admin_user import create_admin_user
from business_service.tests.utils.create_business_profile import create_business_profile

from business_service.models.business_product import BusinessProduct
from business_service.models.business_product_step import BusinessProductStep
from accounts.models.admin_data_confirm import AdminDataConfirm



class TestProductStep(APITestCase):

    accept_product_step_url = reverse('admin_accept_product_step', kwargs={'prod_step_id': 1})
    reject_product_step_url = reverse('admin_reject_product_step', kwargs={'prod_step_id': 1})

    def test_accept_product_step(self):

        user = create_admin_user()
        profile = create_business_profile(user)
        self.client.force_authenticate(user)

        product = BusinessProduct.objects.create(business_profile=profile,
                                                 title='app',
                                                 description='...')

        product_step = BusinessProductStep.objects.create(business_product=product,
                                                          note='...',
                                                          step_url='https://google.com',
                                                          from_date='2022-11-03',
                                                          to_date='2020-11-04',
                                                          step_number=1)

        AdminDataConfirm.objects.create(target=product_step)

        post_data = {'comment': 'accepted'}

        self.client.post(self.accept_product_step_url, post_data)

        cnt = ContentType.objects.get_for_model(product_step)

        admin_confirm = get_object_or_404(AdminDataConfirm,
                                          target_ct=cnt,
                                          target_id=product_step.id)

        assert admin_confirm.is_confirmed is True

    def test_reject_product_step(self):

        user = create_admin_user()
        profile = create_business_profile(user)
        self.client.force_authenticate(user)

        product = BusinessProduct.objects.create(business_profile=profile,
                                                 title='app',
                                                 description='...')

        product_step = BusinessProductStep.objects.create(business_product=product,
                                                          note='...',
                                                          step_url='https://google.com',
                                                          from_date='2022-11-03',
                                                          to_date='2020-11-04',
                                                          step_number=1)

        AdminDataConfirm.objects.create(target=product_step)

        post_data = {'comment': 'rejected'}

        self.client.post(self.reject_product_step_url, post_data)

        cnt = ContentType.objects.get_for_model(product_step)

        admin_confirm = get_object_or_404(AdminDataConfirm,
                                          target_ct=cnt,
                                          target_id=product_step.id)

        assert admin_confirm.is_confirmed is False
