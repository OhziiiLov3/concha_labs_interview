# Generated by Django 4.1.1 on 2022-09-26 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_alter_useraccount_options_useraccount_userid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='userId',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]