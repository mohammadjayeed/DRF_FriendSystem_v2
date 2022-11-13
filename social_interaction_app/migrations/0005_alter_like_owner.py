# Generated by Django 4.1.3 on 2022-11-13 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0013_alter_friendship_status'),
        ('social_interaction_app', '0004_alter_like_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_link', to='social_app.profile'),
        ),
    ]
