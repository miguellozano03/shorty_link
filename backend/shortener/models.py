from django.db import models
from django.conf import settings

class Url(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="urls",
    )
    title = models.CharField(max_length=100, blank=True, null=True)
    long_url = models.URLField()
    code  = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)