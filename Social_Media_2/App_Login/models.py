from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')

    full_name = models.CharField(max_length=50, verbose_name='Full Name', blank=True)
    description = models.TextField(verbose_name='Description', blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, verbose_name="Profile Picture")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    facebook_id = models.URLField(blank=True, verbose_name="Facebook Id")
    website_address = models.URLField(blank=True)


class Follow(models.Model):

    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_following")

    