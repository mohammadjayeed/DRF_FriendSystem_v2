# Generated by Django 4.1.3 on 2022-11-13 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_interaction_app', '0008_alter_like_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='value',
        ),
        migrations.AddField(
            model_name='like',
            name='liked',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default=None, max_length=8),
            preserve_default=False,
        ),
    ]
