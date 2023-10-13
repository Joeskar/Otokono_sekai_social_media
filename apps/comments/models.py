from django.db import models
from django.conf import settings


class AbstractComment(models.Model):
    """Abstract model for comments"""
    text = models.TextField(500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True
