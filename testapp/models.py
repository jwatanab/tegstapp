from django.db import models

class Account(models.Model):
  
  name     = models.CharField(max_length=128)
  password = models.CharField(max_length=128)
