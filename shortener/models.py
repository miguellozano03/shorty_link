from django.db import models

class Url(models.Model):
    long_url = models.URLField()
    short_url  = models.CharField(max_length=20)