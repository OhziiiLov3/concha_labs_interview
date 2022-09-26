from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


# Create User Account Model , Django adds user Id Automatically for us 

class UserAccount(models.Model):     
    userId = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image =  models.ImageField(null=True,blank=True)
    audio_data = models.JSONField(default='{}')


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'useraccount'