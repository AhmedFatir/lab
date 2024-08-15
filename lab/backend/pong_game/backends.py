# pong_game/backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailOrUsernameBackend(ModelBackend):
    """
    Custom Authentication Backend that allows authentication using either
    an email address or a username.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Try to fetch the user by username
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            # If username lookup fails, try to fetch by email
            try:
                user = UserModel.objects.get(email=username)
            except UserModel.DoesNotExist:
                return None

        if user.check_password(password):
            return user
        return None
