from django.db import models

# Create your models here.
class Login(models.Model):
    name=models.CharField(max_length=40)
    Password=models.CharField(max_length=40)
