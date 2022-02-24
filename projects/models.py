from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=50, blank=False)
    discription = models.TextField(max_length=200, null=True)
    admin = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    pending_tasks = models.TextField(max_length=120, blank=True)
    working_tasks = models.TextField(max_length=120, blank=True)
    completed_tasks = models.TextField(max_length=120, blank=True)