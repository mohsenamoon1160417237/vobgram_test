from django.urls import path

from .views.add_pre_order_service import AddPreOrderService
from .views.customer_register import CustomerRegisterPreOrderService
from .views.customer_unregister import CustomerUnRegisterPreOrderService

from .views.owner_list import OwnerPreOrderServiceList
from .views.list import PreOrderServiceList

urlpatterns = [

    path('add/<int:ord_id>/', AddPreOrderService.as_view(), name='edit_get_service'),
    path('add/', AddPreOrderService.as_view(), name='add_service'),
    path('register/<int:ord_id>/', CustomerRegisterPreOrderService.as_view(), name='customer_register_service'),
    path('unregister/<int:ord_id>/', CustomerUnRegisterPreOrderService.as_view(), name='customer_unregister_service'),

    path('owner/list/', OwnerPreOrderServiceList.as_view(), name='owner_service_list'),
    path('list/', PreOrderServiceList.as_view(), name='service_list'),
]
