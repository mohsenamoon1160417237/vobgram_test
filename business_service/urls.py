from django.urls import path

from .views.skill.search_valid_skill import SearchValidSkill
from .views.skill.add_valid_skill import AddValidSkill
from .views.skill.choose_skill import ChooseBusinessSkill

from .views.search_business_profile import SearchBusinessProfile
from .views.view_profile import ViewProfile
from .views.add_business_product import AddBusinessProduct


urlpatterns = [

    path('search_skill/<str:query>/', SearchValidSkill.as_view(), name='search_valid_skill'),
    path('add_skill/', AddValidSkill.as_view(), name='add_valid_skill'),
    path('choose_skill/', ChooseBusinessSkill.as_view(), name='choose_skill'),
    path('search_business_profile/<str:query>/', SearchBusinessProfile.as_view(), name='search_business_profile'),
    path('profile/<int:id>/', ViewProfile.as_view(), name='view_profile'),
    path('add_product/', AddBusinessProduct.as_view(), name='add_get_business_product'),
    path('add_product/<int:prod_id>/', AddBusinessProduct.as_view(), name='update_delete_business_product')
]
