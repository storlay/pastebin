from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Text(models.Model):
    uuid_url = models.UUIDField(unique=True, editable=False)
    drive_id = models.CharField(max_length=33)
    is_temporary = models.BooleanField(default=False)
    datetime_of_deletion = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', blank=True, null=True)
    datetime_of_creation = models.DateTimeField(auto_now_add=True)
