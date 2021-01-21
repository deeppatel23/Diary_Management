from django.db import models
import datetime
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class memory(models.Model):
    title = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField('Created', auto_now_add=True)
    updated_at = models.DateTimeField('Updated', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, )