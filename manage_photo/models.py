from django.db import models

# Create your models here.

class PictureModel(models.Model):
    picture = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=50,blank=True,null=True)

class CreateModel(models.Model):
    class_name = models.CharField(max_length=30,blank=True,null=True)