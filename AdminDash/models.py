from django.db import models

department = [
    ('SR', 'Surgeon'),
    ('NS', 'Nurse'),
    ('PD', 'Pedeatrician'),
    ('DR', 'Doctor'),
    ('PS', 'Psychaitrist'),
]

# Create your models here.
    
class Physician(models.Model):
    SR = 'Surgeon'
    NS = 'Nurse'
    PD = 'Pedeatrician'
    DR = 'Doctor'
    PS = 'Psychaitrist'
    department = [
    ('SR', 'Surgeon'),
    ('NS', 'Nurse'),
    ('PD', 'Pedeatrician'),
    ('DR', 'Doctor'),
    ('PS', 'Psychaitrist'),
    ]

    name = models.CharField(max_length=100, null=False, blank=True)
    email = models.EmailField(unique=True, null=False, blank=True)
    age = models.IntegerField(null=False, max_length=3)
    phone = PhoneField(null = False, help_text='Contact phone number')
    address = models.Charfield(max_length=250, null=False)
    bio = models.TextField(null=False,max_length=250)
    department = models.CharField(max_length=25, default= DR, choices=department)

    def __str__(self):
        return str(self.name)



    
