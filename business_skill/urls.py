from django.urls import path

from .views.business_specialty.list import ServerBusinessSpecialtyList
from .views.business_specialty.add import ServerAddBusinessSpecialty

from .views.skill.choose import ChooseBusinessSkill
from .views.skill.add_valid import AddValidSkill
from .views.skill.search_valid import SearchValidSkill
from .views.skill.private_list import PrivateUserBusinessSkillList

from .views.search_business_profile import SearchBusinessProfile


urlpatterns = [

    path('list/business_specialty/', ServerBusinessSpecialtyList.as_view(), name='business_specialty_list'),
    path('add/business_specialty/', ServerAddBusinessSpecialty.as_view(), name='add_business_specialty'),
    path('edit/business_specialty/<int:spec_id>/', ServerAddBusinessSpecialty.as_view(),
         name='edit_get_business_specialty'),

    path('search_skill/<str:query>/', SearchValidSkill.as_view(), name='search_valid_skill'),
    path('add_skill/', AddValidSkill.as_view(), name='add_valid_skill'),
    path('choose_skill/', ChooseBusinessSkill.as_view(), name='choose_skill'),
    path('list/skills/', PrivateUserBusinessSkillList.as_view(), name='user_business_skill_list'),

    path('search_business_profile/<str:query>/', SearchBusinessProfile.as_view(), name='search_business_profile'),

]