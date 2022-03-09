from django.urls import path

from .views.valid_skill.accept import AdminAcceptValidSkill
from .views.valid_skill.reject import AdminRejectValidSKill
from .views.valid_skill.list import AdminNotconfirmedValidSkillList

from .views.business_data.accept import AdminAcceptBusinessData
from .views.business_data.reject import AdminRejectBusinessData
from .views.business_data.list import AdminNotConfirmedBusinessDataList

from .views.business_product_step.accept import AdminAcceptBusinessProductStep
from .views.business_product_step.reject import AdminRejectBusinessProductStep

from .views.business_product.accept import AdminAcceptBusinessProduct
from .views.business_product.reject import AdminRejectBusinessProduct
from .views.business_product.list import AdminNotConfirmedBusinessProductList

from .views.business_specialty.list import AdminNotConfirmedBusinessSpecialtyList
from .views.business_specialty.accept import AdminBusinessSpecialtyAccept
from .views.business_specialty.reject import AdminBusinessSpecialtyReject

from .views.contract_assign.list import ContractAssignList

from .views.service_request.list import AdminNotConfirmedServiceRequestList
from .views.service_request.accept import AdminAcceptServiceRequest
from .views.service_request.reject import AdminRejectServiceRequest

from .views.service_contract.join import SupVisorJoinContract
from .views.service_contract.leave import SupVisorLeaveContract

from .views.pre_order_service.list import NotConfirmedAdminPreOrderServiceList
from .views.pre_order_service.accept import AdminAcceptPreOrderService


urlpatterns = [

    path('list/valid_skills/', AdminNotconfirmedValidSkillList.as_view(), name='admin_valid_skills_list'),
    path('list/business_data/', AdminNotConfirmedBusinessDataList.as_view(), name='admin_business_data_list'),
    path('list/business_product/', AdminNotConfirmedBusinessProductList.as_view(), name='admin_business_product_list'),
    path('valid_skill/accept/<int:skill_id>/', AdminAcceptValidSkill.as_view(), name='admin_accept_valid_skill'),
    path('valid_skill/reject/<int:skill_id>/', AdminRejectValidSKill.as_view(), name='admin_reject_valid_skill'),

    path('business_data/accept/<int:prof_id>/<str:data_type>/', AdminAcceptBusinessData.as_view(),
         name='admin_accept_business_data'),

    path('business_data/reject/<int:prof_id>/<str:data_type>/', AdminRejectBusinessData.as_view(),
         name='admin_reject_business_data'),

    path('product_step/accept/<int:prod_step_id>/', AdminAcceptBusinessProductStep.as_view(),
         name='admin_accept_product_step'),

    path('product_step/reject/<int:prod_step_id>/', AdminRejectBusinessProductStep.as_view(),
         name='admin_reject_product_step'),

    path('product/accept/<int:prod_id>/', AdminAcceptBusinessProduct.as_view(),
         name='admin_accept_product'),

    path('product/reject/<int:prod_id>/', AdminRejectBusinessProduct.as_view(),
         name='admin_reject_product'),

    path('list/specialties/', AdminNotConfirmedBusinessSpecialtyList.as_view(), name='admin_business_specialty_list'),
    path('specialty/accept/<int:spec_id>/', AdminBusinessSpecialtyAccept.as_view(),
         name='admin_accept_business_specialty'),

    path('specialty/reject/<int:spec_id>/', AdminBusinessSpecialtyReject.as_view(),
         name='admin_reject_business_specialty'),

    path('list/contract_assigns/', ContractAssignList.as_view(), name='admin_contract_assigns_list'),

    path('list/service_requests/', AdminNotConfirmedServiceRequestList.as_view(), name='admin_service_requests_list'),
    path('accept/service_request/<int:req_id>/', AdminAcceptServiceRequest.as_view(), name='admin_accept_service_request'),
    path('reject/service_request/<int:req_id>/', AdminRejectServiceRequest.as_view(), name='admin_reject_service_request'),

    path('contract/join/<int:cont_id>/', SupVisorJoinContract.as_view(), name='sup_vs_join_contract'),
    path('contract/leave/<int:cont_id>/', SupVisorLeaveContract.as_view(), name='sup_vs_leave_contract'),

    path('list/pre_order_service/', NotConfirmedAdminPreOrderServiceList.as_view(),
         name='admin_pre_order_service_list'),

    path('accept/pre_order_service/<int:ord_id>/', AdminAcceptPreOrderService.as_view(),
         name='admin_accept_pre_order_service'),

    path('reject/pre_order_service/<int:ord_id>/', AdminRejectServiceRequest.as_view(),
         name='admin_reject_pre_order_service')

]
