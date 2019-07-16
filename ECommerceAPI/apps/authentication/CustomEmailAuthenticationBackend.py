from ECommerceAPI.apps.authentication.models import User


class EmailAuthBackend():
    def authenticate(self, request, email, password):
        try:
            user = User.objects.get(email=email)
            success = user.check_password(password)
            if success:
                return user
        except User.DoesNotExist:
            pass
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
