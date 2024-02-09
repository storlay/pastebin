from django.db import models


class Text(models.Model):
    url_hash = models.TextField()