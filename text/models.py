from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Text(models.Model):
    url_hash = models.TextField()
    is_temporary = models.BooleanField(default=False)
    datetime_of_deletion = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', blank=True, null=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("show_message", kwargs={"pk": self.pk})
