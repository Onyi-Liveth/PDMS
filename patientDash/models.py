from django.db import models

# Create your models here.
patientID = models.CharField(unique=True, null=False, primary_key=True)
pat_name = models.CharField(max_length=100, null=False)
pat_email = models.EmailField(unique=True, null=False)
pat_number = PhoneField(blank=False, help_text='Contact phone number')
pat_gender = models.BooleanField(default=True)
pat_DOB = models.DateTimeField(auto_now=True)
pat_address = models.Charfield(max_length=250, null=False)
next_of_kin = models.CharField(max_length=100, null=False)
pat_age = models.IntegerField(null=False, max_length=3)
occupation = models.TextField(blank=False, max_length=50 )