# Generated by Django 4.0.3 on 2022-07-29 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
