import uuid

from django.db import models

from .helpers import generate_key


class APIKey(models.Model):

    class Meta:
        verbose_name_plural = "API Keys"
        ordering = ['-created']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50, unique=True)
    service = models.CharField(max_length=50)
    key = models.CharField(
        max_length=40, unique=True,
        default=generate_key
    )

    def __str__(self):
        return self.name
