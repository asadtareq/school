from django.db import models

# Create your models here.
class notice(models.Model):
    notice_title=models.CharField(max_length=255)
    notice_description=models.ImageField()
    notice_date=models.DateField()

class Head_Master_Message(models.Model):
    image=models.ImageField()
    message=models.TextField()
    
    def __str__(self):
        return self.message

class Gallery(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField()

class Sliders(models.Model):
    title=models.CharField(max_length=255)
    short_description=models.CharField(max_length=255)
    image=models.ImageField()
    
class smc(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField()
    date=models.DateField()
    
#club
class club(models.Model):
    menu= (
        ('1','Language'),
        ('2','Debate'),
        ('3','ICT'),
        ('4','Chess'),
        ('5','Math'),
        ('6','Science'),
    )
    title = models.CharField(max_length=255)
    image = models.ImageField()
    page = models.CharField(max_length=255,default="SELECT", choices=menu) 

#result
class result(models.Model):
    sid=models.CharField(max_length=255)