from django.db import models

# Create your models here.

class logindb (models.Model):
    username = models.CharField(max_length=20,null=True,blank=True)
    e_mail = models.EmailField(max_length=20,null=True,blank=True)
    password = models.CharField(max_length=20,null=True,blank=True)



