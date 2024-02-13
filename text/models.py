from django.db import models


class Text(models.Model):
    url_hash = models.TextField()
    is_temporary = models.BooleanField(default=False)
    datetime_of_deletion = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("input_text", kwargs={"hash": self.url_hash})