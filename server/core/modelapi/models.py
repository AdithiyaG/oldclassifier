from django.db import models

# Create your models here.
class PatientAPI(models.Model):
    Id=models.AutoField(primary_key=True)
    MedicalId=models.PositiveIntegerField()
    PatientName=models. CharField(max_length=100)
    PatientGender=models. CharField(max_length=6)
    PatientAge=models.PositiveIntegerField()
    PatientDOB=models.DateField()
    PatientHeight=models.PositiveIntegerField()
    PatientWeight=models.PositiveIntegerField()
    UserId=models.CharField(max_length=500)
    DateCreated=models.DateField(auto_now_add=True)

class ClassifierAPI(models.Model):
    Id=models.AutoField(primary_key=True)
    MedicalId=models.PositiveIntegerField()
    Class=models.CharField(max_length=100)
    Accuracy=models.PositiveIntegerField()
    ImagePath=models.ImageField()
    UserId=models.CharField(max_length=500)
    UsedDate=models.DateField(auto_now_add=True)
    