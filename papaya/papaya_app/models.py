from django.db import models
from django.conf import settings

# Create your models here.

class Papaya(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)