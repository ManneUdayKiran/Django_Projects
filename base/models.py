from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200,blank=True,null=True)
    description=models.CharField(max_length=120,blank=True,null=True)
