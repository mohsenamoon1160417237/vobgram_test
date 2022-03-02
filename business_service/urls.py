from django.urls import path

from .views.skill.search_valid import SearchValidSkill
from .views.skill.add_valid import AddValidSkill
from .views.skill.choose import ChooseBusinessSkill
from .views.skill.private_list import PrivateUserBusinessSkillList

from .views.search_business_profile import SearchBusinessProfile
from .views.view_profile import ViewProfile

from .views.business_product.add import AddBusinessProduct
from .views.business_product.add_step import AddBusinessProductStep
from .views.business_product.private_list import PrivateUserBusinessProductList
from .views.business_product.vote import AddBusinessProductVote

from .views.service_request.customer_add import CustomerAddServiceRequest
from .views.service_request.customer_send import CustomerSendServiceRequest
from .views.service_request.server_bid import ServerServiceRequestBid
from .views.service_request.customer_bid_list import ServiceRequestBidList
from .views.service_request.customer_accept_bid import CustomerAcceptBid
from .views.service_request.add_review import AddServiceReview
from .views.service_request.customer_add_skill import CustomerAddSkillToServiceRequest

from .views.service_request.list.customer import CustomerServiceRequestList
from .views.service_request.list.server_received import ServerReceivedServiceRequestList

from .views.business_specialty.add import ServerAddBusinessSpecialty
from .views.business_specialty.list import ServerBusinessSpecialtyList


urlpatterns = [

    path('search_skill/<str:query>/', SearchValidSkill.as_view(), name='search_valid_skill'),
    path('add_skill/', AddValidSkill.as_view(), name='add_valid_skill'),
    path('choose_skill/', ChooseBusinessSkill.as_view(), name='choose_skill'),
    path('list/skills/', PrivateUserBusinessSkillList.as_view(), name='user_business_skill_list'),
    path('search_business_profile/<str:query>/', SearchBusinessProfile.as_view(), name='search_business_profile'),
    path('profile/<int:id>/', ViewProfile.as_view(), name='view_profile'),
    path('add_product/', AddBusinessProduct.as_view(), name='add_business_product'),
    path('add_product/<int:prod_id>/', AddBusinessProduct.as_view(), name='edit_get_business_product'),
    path('list/products/', PrivateUserBusinessProductList.as_view(), name='user_business_product_list'),
    path('add_product_step/<int:prod_id>/', AddBusinessProductStep.as_view(), name='add_business_product_step'),

    path('edit_product_step/<int:prod_step_id>/', AddBusinessProductStep.as_view(),
         name='edit_get_business_product_step'),

    path('vote_business_product/<int:prod_id>/', AddBusinessProductVote.as_view(), name='add_business_product_vote'),
    path('vote_business_product/<int:vote_id>/', AddBusinessProductVote.as_view(), name='delete_get_business_product_vote'),
    path('add_service_request/', CustomerAddServiceRequest.as_view(), name='add_service_request'),

    path('edit_get_service_request/<int:serv_id>/', CustomerAddServiceRequest.as_view(),
         name='edit_get_service_request'),

    path('send_service_request/<int:prof_id>/<int:serv_id>/', CustomerSendServiceRequest.as_view(), name='send_service_request'),
    path('bid_service_request/<int:serv_id>/', ServerServiceRequestBid.as_view(), name='bid_service_request'),
    path('accept_bid/<int:bid_id>/', CustomerAcceptBid.as_view(), name='customer_accept_bid'),
    path('add/review/<int:serv_id>/', AddServiceReview.as_view(), name='add_service_review'),
    path('add/service_request/skill/<int:req_id>/<str:skill_ttl>/', CustomerAddSkillToServiceRequest.as_view(),
         name='customer_add_skill_to_service_request'),
    path('list/customer/service_requests/', CustomerServiceRequestList.as_view(), name='customer_service_request_list'),
    path('list/server/service_requests/', ServerReceivedServiceRequestList.as_view(), name='server_service_request_list'),
    path('list/bids/<int:serv_id>/', ServiceRequestBidList.as_view(), name='service_request_bid_list'),

    path('add/business_specialty/', ServerAddBusinessSpecialty.as_view(), name='add_business_specialty'),
    path('edit/business_specialty/<int:spec_id>/', ServerAddBusinessSpecialty.as_view(),
         name='edit_get_business_specialty'),
    path('list/business_specialty/', ServerBusinessSpecialtyList.as_view(), name='business_specialty_list')
]
