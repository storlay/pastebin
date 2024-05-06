"""
Configuration of models for the database
"""

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model"""

    pass
