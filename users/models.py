from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_name = models.CharField(max_length=10)
    role = models.CharField(max_length=10, default='member')
    projects = models.CharField(max_length=500)