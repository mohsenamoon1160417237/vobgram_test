from django.urls import path
from .views.Home import HomeView
from rest_framework_simplejwt.views import TokenRefreshView
from accounts.views.authorization.logout import LogoutView
from accounts.views.authorization.check_phone_number import CheckPhoneNumber
from accounts.views.authorization.create_tokens import CreateTokens
from accounts.views.update_profile.first_step import UpdateProfileFirstStep
from accounts.views.update_profile.change_password import ChangePassword
from accounts.views.update_profile.business import BusinessData



urlpatterns = [

    path('phone_number/', CheckPhoneNumber.as_view(), name='check_phone_number'),
    path('create_token/', CreateTokens.as_view(), name='create_tokens'),
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('update_profile/first_step/', UpdateProfileFirstStep.as_view(), name='update_profile_first_step'),
    path('update_profile/change_password/', ChangePassword.as_view(), name='update_profile_change_password'),
    path('update_profile/business_data/', BusinessData.as_view(), name='update_business_data'),
]
