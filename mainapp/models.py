from django.db import models

# Create your models here.

class Security(models.Model):
    full_name = models.CharField(max_length=70)
    specialty = models.CharField(max_length=55)
    images = models.ImageField(upload_to='security/')


    def __str__(self):
        return self.full_name
    
class About(models.Model):
    toliq_name =models.CharField(max_length=80)
    muttaxasisligi = models.CharField(max_length=60)
    rasmi = models.ImageField(upload_to='about/') 


    def __str__(self):
        return self.toliq_name