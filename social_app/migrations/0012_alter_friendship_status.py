# Generated by Django 4.1.3 on 2022-11-12 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0011_alter_friendship_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='status',
            field=models.CharField(choices=[('send', 'send'), ('accepted', 'accepted')], max_length=12),
        ),
    ]