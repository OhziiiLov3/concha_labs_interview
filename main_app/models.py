from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField



# Create your models here.


# Create User Account Model , Django adds user Id Automatically for us 

class UserAccount(models.Model):
    userId = models.CharField(max_length=20)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    image =  models.ImageField(null=True,blank=True)
    audio_data = models.JSONField(default='{}')


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'useraccount'

class AudioData(models.Model):
    ticks = ArrayField(
        ArrayField(
            models.CharField(max_length=15, blank=True),
            size=8,
        ),
        size=8,
    )
    session_id = models.CharField(max_length=20, unique=True)
    step_count = models.CharField(max_length=9, unique=True)
    select_tick = models.CharField(max_length=14)

    def __str__(self):
        return self.session_id


class Meta:
    db_table = 'concha_audio'
