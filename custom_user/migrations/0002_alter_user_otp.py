# Generated by Django 4.1.3 on 2022-11-10 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otp',
            field=models.CharField(default=9017, max_length=4),
        ),
    ]