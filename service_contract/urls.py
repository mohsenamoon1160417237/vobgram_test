from django.urls import path

from .views.contract_assign.customer import CustomerAssignContract
from .views.contract_assign.get import GetContractAssign
from .views.contract_assign.server import ServerAssignContract

urlpatterns = [

    path('contract_assigns/get/<int:ctr_asgn_id>/', GetContractAssign.as_view(), name='get_contract_assign'),
    path('contract_assign/customer/<int:ctr_asgn_id>/', CustomerAssignContract.as_view(),
         name='customer_assign_contract'),
    path('contract_assign/server/<int:ctr_asgn_id>/', ServerAssignContract.as_view(),
         name='server_assign_contract')

]
