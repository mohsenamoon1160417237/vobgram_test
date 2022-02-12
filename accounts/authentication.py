from accounts.models.UserRegistration import UserRegistration

class EmailAuthentication(object):

    def authenticate(self, request, username=None, password=None):

        try:
            user = UserRegistration.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except UserRegistration.DoesNotExist:
            return None


    def get_user(self, user_id):

        try:
            return UserRegistration.objects.get(id=user_id)
        except UserRegistration.DoesNotExist:
            return None
