# Generated by Django 4.1.1 on 2022-09-26 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_useraccount_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='userId',
            field=models.PositiveIntegerField(default=0),
        ),
    ]