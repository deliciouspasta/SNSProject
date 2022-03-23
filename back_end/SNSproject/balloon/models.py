# from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)

#     def __str__(self):
#         return self.name

# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(max_length=100, unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = [email, username]
#     class Meta:
#         verbose_name_plural = 'CustomUser'

class PostBalloon(models.Model):
    # author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(upload_to='static/rest_framework/media/', blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.author