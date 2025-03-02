from django.contrib.auth import get_user_model

from account.models import Profile

UserModel = get_user_model()


def create_profile(backend, user, *args, **kwargs):
    """Create user profile for social authentication."""
    Profile.objects.get_or_create(user=user)


class EmailAuthBackend:
    """
    Authenticate (login) using an e-mail address as username.
    - Django provides a simple way to define your own authentication backends. An authentication backend is a simple
      class that provides 'authenticate' and 'get_user' methods.
      * 'authenticate': takes 'request' object and user credentials as parameters and returns a user object
      * 'get_user': takes an id as parameter and returns a user object
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = UserModel.objects.get(email=username)
            if user.check_password(password):
                return user
        except (UserModel.DoesNotExist, UserModel.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExit:
            return None
