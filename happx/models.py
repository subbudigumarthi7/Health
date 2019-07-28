from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.

class patmodels(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    sex = models.CharField(max_length=5)
    problem = models.TextField(max_length=50)
    DoctorType=models.CharField(max_length=20)

    def __str__(self):
        return self.sex



class Doctor(models.Model):
    Patmodels=models.ForeignKey(patmodels,on_delete=models.CASCADE)
    Gender=models.CharField(max_length=10)
    specilization =models.CharField(max_length=10)
    Qualification=models.CharField(max_length=10)
    Email=models.EmailField(max_length=30)

    def __str__(self):
        return self.Gender




