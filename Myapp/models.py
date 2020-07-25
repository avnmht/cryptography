from django.db import models

# Create your models here.
class activusers(models.Model):
    username=models.CharField(max_length=20)
    authtoken=models.CharField(max_length=20)

