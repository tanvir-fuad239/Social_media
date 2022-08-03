from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    
    post_image = models.ImageField(upload_to="post_images",verbose_name="Upload an image")
    caption = models.CharField(max_length=1000,verbose_name="What is on your mind?", blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-upload_date', )



class Like(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="liked_post")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_user")

    

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user")
    comment = models.TextField(verbose_name="Your comment", blank=False)
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date', )

        







