# Generated by Django 4.1.1 on 2022-09-26 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_useraccount_user_useraccount_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='userId',
        ),
    ]