# Generated by Django 4.1.3 on 2022-11-13 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_interaction_app', '0003_alter_comment_post_alter_like_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], max_length=8),
        ),
    ]