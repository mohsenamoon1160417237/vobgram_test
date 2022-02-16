from django.urls import path

from .views.list.valid_skill import AdminNotconfirmedValidSkillList
from .views.list.business_data import AdminNotConfirmedBusinessDataList
from .views.list.business_product import AdminNotConfirmedBusinessProductList

from .views.valid_skill.accept import AdminAcceptValidSkill
from .views.valid_skill.reject import AdminRejectValidSKill

from .views.business_data.accept import AdminAcceptBusinessData
from .views.business_data.reject import AdminRejectBusinessData

from .views.business_product_step.accept import AdminAcceptBusinessProductStep
from .views.business_product_step.reject import AdminRejectBusinessProductStep

from .views.business_product.accept import AdminAcceptBusinessProduct
from .views.business_product.reject import AdminRejectBusinessProduct


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
         name='admin_reject_product')
]
