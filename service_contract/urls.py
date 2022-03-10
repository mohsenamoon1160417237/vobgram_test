from django.urls import path

from .views.contract_assign.customer import CustomerAssignContract
from .views.contract_assign.get import GetContractAssign
from .views.contract_assign.server import ServerAssignContract

from .views.direct_contract.customer_add import CustomerDirectContract
from .views.direct_contract.add_skill import AddSkillToContract


urlpatterns = [

    path('contract_assigns/get/<int:ctr_asgn_id>/', GetContractAssign.as_view(), name='get_contract_assign'),
    path('contract_assign/customer/<int:ctr_asgn_id>/', CustomerAssignContract.as_view(),
         name='customer_assign_contract'),
    path('contract_assign/server/<int:ctr_asgn_id>/', ServerAssignContract.as_view(),
         name='server_assign_contract'),

    path('customer/direct_contract/<int:user_id>/', CustomerDirectContract.as_view(),
         name='customer_add_direct_contract'),

    path('customer/direct_contract/<int:ctr_id>/', CustomerDirectContract.as_view(),
         name='customer_get_direct_contract'),

    path('customer/skill/add/<int:ctr_id>/<str:skill_ttl>/', AddSkillToContract.as_view(),
         name='add_skill_to_contract'),

]
