from django.db import models

# Create your models here.
class Patient(models.Model):
  pat_name = models.CharField(max_length=100, null=True)
  pat_email = models.EmailField(unique=True, null=True)
  pat_number = PhoneField(blank=False, help_text='Contact phone number')
  pat_gender = models.BooleanField(default=True)
  pat_DOB = models.DateField(auto_now=True)
  pat_address = models.Charfield(max_length=250, null=True)
  next_of_kin = models.CharField(max_length=100, null=True)
  pat_age = models.IntegerField(null=True, max_length=3)
  occupation = models.TextField(max_length=50)
  reg_date = models.DateField(auto_now=True)
  

  @property
  def patientID(self):
    return str(self.pat_name)

