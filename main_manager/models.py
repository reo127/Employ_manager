from django.db import models
import datetime

# Create your models here.

class Employe(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.IntegerField() 
    address = models.CharField(max_length=70)
    sells = models.IntegerField()
    timeStamp = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name

class ChildEmploye(models.Model):
    ChildSno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    parentEmploye = models.ForeignKey(Employe, on_delete=models.CASCADE)

    
    
