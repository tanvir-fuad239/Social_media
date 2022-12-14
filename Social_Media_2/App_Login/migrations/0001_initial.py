# Generated by Django 4.0.3 on 2022-07-25 06:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Full Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics', verbose_name='Profile Picture')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('facebook_id', models.URLField(blank=True, null=True, verbose_name='Facebook Id')),
                ('website_address', models.URLField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
