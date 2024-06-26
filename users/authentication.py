"""
Custom authentication methods
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

User = get_user_model()


class EmailAuthenticationBackend(BaseBackend):
    """Email authentication"""

    def authenticate(
        self, request, username=None, password=None, **kwargs
    ) -> User | None:
        try:
            user_object = User.objects.get(email=username)
            if user_object.check_password(password):
                return user_object
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id: int) -> User | None:
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
