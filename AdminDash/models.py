from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Admin(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    adminID = models.IntegerField(unique=True, null=True, primary_key=True)
    bio = models.TextField(null=True, blank=True)
    description = models.TextField(max_length=250, blank=True)
    is_professional = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


