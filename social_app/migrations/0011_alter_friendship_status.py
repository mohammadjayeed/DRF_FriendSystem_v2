# Generated by Django 4.1.3 on 2022-11-11 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0010_alter_friendship_status_alter_profile_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='status',
            field=models.CharField(choices=[('accepted', 'accepted'), ('send', 'send')], max_length=12),
        ),
    ]
