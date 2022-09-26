from django.contrib import admin

# Register your models here.

from .models import AudioData, UserAccount

admin.site.register(UserAccount)
admin.site.register(AudioData)