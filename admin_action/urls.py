from django.urls import path

from .views.list.valid_skill import AdminNotconfirmedValidSkillList
from .views.list.business_data import AdminBusinessDataList
from .views.list.business_product import AdminBusinessProductList

from .views.valid_skill.accept import AdminAcceptValidSkill
from .views.valid_skill.reject import AdminRejectValidSKill

from .views.business_data.accept import AdminAcceptBusinessData
from .views.business_data.reject import AdminRejectBusinessData


urlpatterns = [

    path('list/valid_skills/', AdminNotconfirmedValidSkillList.as_view(), name='admin_valid_skills_list'),
    path('list/business_data/', AdminBusinessDataList.as_view(), name='admin_business_data_list'),
    path('list/business_product/', AdminBusinessProductList.as_view(), name='admin_business_product_list'),
    path('valid_skill/accept/<int:skill_id>/', AdminAcceptValidSkill.as_view(), name='admin_accept_valid_skill'),
    path('valid_skill/reject/<int:skill_id>/', AdminRejectValidSKill.as_view(), name='admin_reject_valid_skill'),
    path('business_data/accept/<int:prof_id>/<str:data_type>/', AdminAcceptBusinessData.as_view(),
         name='admin_accept_business_data'),
    path('business_data/reject/<int:prof_id>/<str:data_type>/', AdminRejectBusinessData.as_view(),
         name='admin_reject_business_data'),
]
