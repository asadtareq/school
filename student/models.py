from django.db import models

# Create your models here.
class student(models.Model):
    gender= (
        ('Boy','Boy'),
        ('Girl','Girl'),
    )
    name=models.CharField(max_length=255)
    class_name=models.CharField(max_length=255)
    roll=models.CharField(max_length=255)
    mobile=models.CharField(max_length=11)
    gender=models.CharField(max_length=255,default="SELECT", choices=gender) 