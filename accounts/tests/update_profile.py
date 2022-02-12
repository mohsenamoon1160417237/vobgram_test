from rest_framework.test import APITestCase
from django.urls import reverse

from accounts.models.profiles.personal import PersonalProfile
from accounts.models.UserRegistration import UserRegistration
from accounts.models.admin_data_confirm import AdminDataConfirm
from accounts.models.profiles.business import BusinessProfile
from accounts.models.profiles.admin import AdminProfile

from accounts.model_serializers.business_profile import BusinessProfileSerializer

from django.shortcuts import get_object_or_404
from .utils.create_user import create_user
from .utils.create_first_step import create_first_step





class UpdateProfile(APITestCase):

    password_url = reverse('update_profile_change_password')
    first_step_url = reverse('update_profile_first_step')
    business_url = reverse('update_business_data')

    def create_user(self):

        user = UserRegistration.objects.create(phone_number="989366922661",
                                               registered=True,
                                               user_type="normal")
        user.set_password('mohsen12345678')
        user.save()
        return user

    def test_change_password(self):

        user = create_user()
        self.client.force_authenticate(user)
        data = {'current_password': 'mohsen12345678',
                'new_password': 'mohsen12345679'}
        response = self.client.post(self.password_url, data)
        assert user.check_password('mohsen12345679')
        assert response.data['status'] == 'changed password'

    def test_first_step_existing_profile_optional_fields_not_empty(self):

        user = create_user()
        self.client.force_authenticate(user)
        PersonalProfile.objects.create(first_name='first name',
                                       last_name='last name',
                                       user=user)

        test_data = {'first_name': 'first name1',
                     'last_name': 'last name1',
                     'email': 'dramatic225@gmail.com',
                     'username': 'sdfsdf'}

        self.client.post(self.first_step_url, test_data)
        profile = get_object_or_404(PersonalProfile, user=user)
        first_name = profile.first_name
        last_name = profile.last_name
        email = profile.email
        username = profile.username
        assert first_name == 'first name1'
        assert last_name == 'last name1'
        assert email == 'dramatic225@gmail.com'
        assert username == 'sdfsdf'

    def test_first_step_existing_profile_optional_fields_empty(self):

        user = create_user()
        self.client.force_authenticate(user)
        PersonalProfile.objects.create(first_name='first name',
                                       last_name='last name',
                                       user=user)

        test_data = {'first_name': 'first name1',
                     'last_name': 'last name1',
                     'email': "",
                     'username': ""}

        self.client.post(self.first_step_url, test_data)
        profile = get_object_or_404(PersonalProfile, user=user)
        first_name = profile.first_name
        last_name = profile.last_name
        email = profile.email
        username = profile.username
        assert first_name == 'first name1'
        assert last_name == 'last name1'
        assert email == ""
        assert username == ""

    def test_first_step_new_profile_optional_fields_not_empty(self):

        user = create_user()
        self.client.force_authenticate(user)
        test_data = {'first_name': 'first name1',
                     'last_name': 'last name1',
                     'email': "dramatic225@gmail.com",
                     'username': "sdfsdf"}

        self.client.post(self.first_step_url, test_data)
        profiles = PersonalProfile.objects.filter(first_name='first name1')
        assert profiles.exists()
        assert profiles.count() == 1
        profile = profiles[0]
        last_name = profile.last_name
        email = profile.email
        username = profile.username
        assert last_name == 'last name1'
        assert email == 'dramatic225@gmail.com'
        assert username == 'sdfsdf'

    def test_first_step_new_profile_optional_fields_empty(self):

        user = create_user()
        self.client.force_authenticate(user)
        test_data = {'first_name': 'first name1',
                     'last_name': 'last name1',
                     'email': "",
                     'username': ""}

        self.client.post(self.first_step_url, test_data)
        profiles = PersonalProfile.objects.filter(first_name='first name1')
        assert profiles.exists()
        assert profiles.count() == 1
        profile = profiles[0]
        last_name = profile.last_name
        email = profile.email
        username = profile.username
        assert last_name == 'last name1'
        assert email == ""
        assert username == ""

    def test_get_business_data_no_previous_data(self):

        user = create_first_step()
        self.client.force_authenticate(user)
        response = self.client.get(self.business_url)
        data = response.data
        assert data['status'] == 'no data'

    def test_get_business_data_has_previous_data(self):

        user = create_first_step()
        self.client.force_authenticate(user)
        post_data = {'company_name': 'mohsen',
                     'company_phone_number': '23478343',
                     'bio': 'hello',
                     'user_id': user.id}
        serializer = BusinessProfileSerializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = self.client.get(self.business_url)
        data = response.data
        assert data['status'] == 'has data'
        assert data['business_profile'] is not None
        assert data['admin_data_confirms'] is not None
        assert len(data['admin_data_confirms']) == 2

    def test_post_business_data_no_previous_data(self):

        user = create_first_step()
        self.client.force_authenticate(user)

        post_data = {"company_name": "mohsen",
                     "company_phone_number": "2342342",
                     "bio": "hello"}

        response = self.client.post(self.business_url, post_data)
        data = response.data
        assert data['status'] == 'created business data'
        business_profiles = BusinessProfile.objects.filter(user=user)
        assert business_profiles.exists()
        assert business_profiles.count() == 1
        business_profile = business_profiles[0]

        company_name = business_profile.company_name
        company_phone_number = business_profile.company_phone_number
        bio = business_profile.bio

        assert company_name == 'mohsen'
        assert company_phone_number == '2342342'
        assert bio == 'hello'

        admin_confirms = AdminDataConfirm.objects.filter(business_profile=business_profile)
        assert admin_confirms.exists()
        assert admin_confirms.count() == 2

        company_name_admin = admin_confirms.filter(data_type='company_name')[0]
        company_phone_number_admin = admin_confirms.filter(data_type='company_phone_number')[0]

        assert company_name_admin.data_value == 'mohsen'
        assert company_phone_number_admin.data_value == '2342342'

    def test_post_business_data_has_previous_data_admin_not_confirmed(self):

        user = create_first_step()
        self.client.force_authenticate(user)
        post_data = {'company_name': 'mohsen',
                     'company_phone_number': '23478343',
                     'bio': 'hello',
                     'user_id': user.id}

        serializer = BusinessProfileSerializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        post_data = {"company_name": "mohsen1",
                     "company_phone_number": "2342342",
                     "bio": "hello2"}

        response = self.client.post(self.business_url, post_data)
        data = response.data

        assert data['status'] == 'updated business data'
        business_profiles = BusinessProfile.objects.filter(user=user)
        assert business_profiles.exists()
        assert business_profiles.count() == 1

        business_profile = business_profiles[0]
        company_name = business_profile.company_name
        company_phone_number = business_profile.company_phone_number
        bio = business_profile.bio

        assert company_name == 'mohsen1'
        assert company_phone_number == '2342342'
        assert bio == 'hello2'

        admin_confirms = AdminDataConfirm.objects.filter(business_profile=business_profile)
        assert admin_confirms.exists()
        assert admin_confirms.count() == 2

        company_name_admin = admin_confirms.filter(data_type='company_name')[0]
        company_phone_number_admin = admin_confirms.filter(data_type='company_phone_number')[0]

        assert company_name_admin.data_value == 'mohsen1'
        assert company_phone_number_admin.data_value == '2342342'

    def test_post_business_data_has_previous_data_admin_confirmed(self):

        user = create_first_step()
        self.client.force_authenticate(user)

        post_data = {'company_name': 'mohsen',
                     'company_phone_number': '23478343',
                     'bio': 'hello',
                     'user_id': user.id}
        serializer = BusinessProfileSerializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        business_profile = serializer.save()
        admin_profile = AdminProfile.objects.create(user=user)
        admin_confirms = AdminDataConfirm.objects.filter(business_profile=business_profile)
        company_name_admin = admin_confirms.filter(data_type='company_name')[0]
        company_phone_number_admin = admin_confirms.filter(data_type='company_phone_number')[0]

        company_name_admin.admin_profile = admin_profile
        company_name_admin.is_confirmed = True
        company_name_admin.save()

        company_phone_number_admin.admin_profile = admin_profile
        company_phone_number_admin.is_confirmed = True
        company_phone_number_admin.save()

        post_data = {"company_name": "mohsen1",
                     "company_phone_number": "2342342",
                     "bio": "hello"}

        response = self.client.post(self.business_url, post_data)
        data = response.data
        assert data['status'] == 'updated business data'
        business_profiles = BusinessProfile.objects.filter(user=user)
        assert business_profiles.exists()
        assert business_profiles.count() == 1
        business_profile = business_profiles[0]
        company_name = business_profile.company_name
        company_phone_number = business_profile.company_phone_number
        assert company_name == 'mohsen1'
        assert company_phone_number == '2342342'

        admin_confirms = AdminDataConfirm.objects.filter(business_profile=business_profile,
                                                         is_latest=True)

        company_name_admin = admin_confirms.filter(data_type='company_name')[0]
        company_phone_number_admin = admin_confirms.filter(data_type='company_phone_number')[0]

        assert company_name_admin.admin_profile is None
        assert company_phone_number_admin.admin_profile is None

