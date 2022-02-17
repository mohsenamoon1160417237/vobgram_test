from rest_framework.test import APITestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404

from accounts.tests.utils.create_first_step import create_first_step
from .utils.create_business_profile import create_business_profile

from business_service.models.service_request import ServiceRequest


class TestServiceRequest(APITestCase):

    add_service_request_url = reverse('add_service_request')
    del_service_request_url = reverse('update_delete_get_service_request', kwargs={'serv_id': 1})
    send_service_request_url = reverse('send_service_request', kwargs={'prof_id': 1,
                                                                       'serv_id': 1})

    def test_add_service_request(self):

        user = create_first_step()
        self.client.force_authenticate(user)

        post_data = {'service_type': 'p',
                     'title': 'title',
                     'note': 'note',
                     'least_budget': 12,
                     'max_budget': 20}

        self.client.post(self.add_service_request_url, post_data)

        requests = ServiceRequest.objects.filter(requester=user.personal_profile,
                                                 service_type='p',
                                                 title='title')

        assert requests.exists()

    def test_delete_service_request(self):

        user = create_first_step()
        self.client.force_authenticate(user)

        ServiceRequest.objects.create(requester=user.personal_profile,
                                      title='p',
                                      note='...',
                                      least_budget=12,
                                      max_budget=20)

        self.client.delete(self.del_service_request_url)

        requests = ServiceRequest.objects.filter(requester=user.personal_profile,
                                                 service_type='p',
                                                 title='title')

        assert not requests.exists()

    def test_send_service_request(self):

        user = create_first_step()
        create_business_profile(user)
        self.client.force_authenticate(user)

        ServiceRequest.objects.create(requester=user.personal_profile,
                                      title='p',
                                      note='...',
                                      least_budget=12,
                                      max_budget=20)

        self.client.post(self.send_service_request_url)

        profile = user.business_profile

        service = get_object_or_404(ServiceRequest,
                                    requester=user.personal_profile,
                                    title='p')

        assert profile in service.receivers.all()
