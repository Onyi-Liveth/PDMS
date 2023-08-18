from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Admin(AbstractUser):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    adminID = models.IntegerField(max_length=10,unique=True, null=False, primary_key=True)
    dob = models.DateField(auto_now=True)
    phone = PhoneField(blank=False, help_text='Contact phone number')
    address = models.Charfield(max_length=250, null=False, blank=False)
    age = models.IntegerField(max_length=3, null=False, blank=False)
    bio = models.TextField(max_length=250, null=False, blank=False)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Physician(models.Model):
    doc_name = models.CharField(max_length=100, null=False, blank=False)
    doc_email = models.EmailField(unique=True, null=False, blank=False)
    doc_ID = models.CharField(unique=True, null=False, primary_key=True)
    doc_dob = models.DateTimeField(auto_now=True, blank=False)
    doc_age = models.IntegerField(null=False, max_length=3)
    doc_phone = PhoneField(blank=False, help_text='Contact phone number')
    doc_address = models.Charfield(max_length=250, null=False, blank=False)
    doc_bio = models.TextField(null=False, blank=False)
    doc_description = models.TextField(max_length=250, blank=True)


    USERNAME_FIELD = 'doc_email'
    REQUIRED_FIELDS = ['username']