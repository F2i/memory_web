from django.db import models
from django.contrib.auth.models import User


class Memory(models.Model):
    location = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(default=None, null=False)
    longtitude = models.FloatField(default=None, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None)
