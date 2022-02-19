from rest_framework.test import APITestCase
from django.urls import reverse
from django.shortcuts import get_object_or_404

from accounts.tests.utils.create_first_step import create_first_step
from .utils.create_business_profile import create_business_profile

from business_service.models.service_request import ServiceRequest
from business_service.models.service_request_bid import ServiceRequestBid
from business_service.models.service_contract import ServiceContract
from business_service.models.service_review import ServiceReview


class TestServiceRequest(APITestCase):

    add_service_request_url = reverse('add_service_request')
    del_service_request_url = reverse('update_delete_get_service_request', kwargs={'serv_id': 1})
    send_service_request_url = reverse('send_service_request', kwargs={'prof_id': 1,
                                                                       'serv_id': 1})
    bid_service_request_url = reverse('bid_service_request', kwargs={'serv_id': 1})
    accept_bid_url = reverse('customer_accept_bid', kwargs={'bid_id': 1})
    add_service_review_url = reverse('add_service_review', kwargs={'serv_id': 1})

    def test_add_service_request(self):

        user = create_first_step()
        self.client.force_authenticate(user)

        post_data = {'service_type': 'p',
                     'title': 'title',
                     'note': 'note',
                     'least_budget': 12,
                     'max_budget': 20,
                     'max_days': 10}

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

    def test_bid_service_request(self):

        user = create_first_step()
        create_business_profile(user)
        self.client.force_authenticate(user)

        request = ServiceRequest.objects.create(requester=user.personal_profile,
                                                title='p',
                                                note='...',
                                                least_budget=12,
                                                max_budget=20)

        request.receivers.add(user.business_profile)
        request.save()

        post_data = {'suggestion_text': 'I can',
                     'price': 20,
                     'days': 11}

        self.client.post(self.bid_service_request_url, post_data)

        bids = ServiceRequestBid.objects.filter(bidder=user.business_profile)

        assert bids.exists()

    def test_accept_bid(self):

        user = create_first_step()
        create_business_profile(user)
        self.client.force_authenticate(user)
        request = ServiceRequest.objects.create(requester=user.personal_profile,
                                                title='p',
                                                note='...',
                                                least_budget=12,
                                                max_budget=20)

        request.receivers.add(user.business_profile)
        request.save()

        bid = ServiceRequestBid.objects.create(bidder=user.business_profile,
                                               service_request=request,
                                               days=5,
                                               price=15)
        self.client.post(self.accept_bid_url)

        request = get_object_or_404(ServiceRequest, id=request.id)

        assert request.finished is True

        contracts = ServiceContract.objects.filter(service_request=request,
                                                   bid=bid)

        assert contracts.exists()

    def test_add_service_review(self):

        user = create_first_step()
        create_business_profile(user)
        self.client.force_authenticate(user)
        request = ServiceRequest.objects.create(requester=user.personal_profile,
                                                title='p',
                                                note='...',
                                                least_budget=12,
                                                max_budget=20)

        request.receivers.add(user.business_profile)
        request.save()

        bid = ServiceRequestBid.objects.create(bidder=user.business_profile,
                                               service_request=request,
                                               suggestion_text='hello',
                                               price=15,
                                               days=5)

        contract = ServiceContract.objects.create(service_request=request,
                                                  server=user.business_profile,
                                                  days=5,
                                                  price=15,
                                                  bid=bid)

        post_data = {'service_rating': 3,
                     'service_note': 'hello'}

        self.client.post(self.add_service_review_url, post_data)

        reviews = ServiceReview.objects.filter(service_request=request,
                                               service_contract=contract)

        assert reviews.exists()
