from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    email = models.EmailField(max_length=50,unique=True)
    username = models.CharField(max_length=25, unique=True)
    phone = models.CharField(max_length=10)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'

    REQUIRED_FIELDS = ['username',]

    
    

class Doctor(User):
    photo = models.ImageField(upload_to='images/doctors')
    degree = models.ImageField(upload_to='images/degrees')
    specialization = models.CharField(max_length=50)
    experience = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    fees = models.IntegerField(default=0)
    bio = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Doctor'
    

class Patient(User):
    reports = models.ImageField(upload_to='images/patients',null=True,blank=True)
    disease = models.CharField(max_length=50)


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Patient'