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
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.author

# class PileColor(models.Model):
#     """Holds the Pile Color, like SALT & PEPPER, Cinnamon"""
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=250)

#     def __str__(self):
#         return self.name


# class HedgeHog(models.Model):
#     """ The Model to hold a list of Hedgehogs """
#     name = models.CharField(max_length=250)
#     pile_color = models.ForeignKey('PileColor', on_delete=models.CASCADE)
#     stars = models.FloatField(default=1.0)
#     description = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# class Comment(models.Model):
#     """Stores Comments by users about the HedgeHog """
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     hedgehog = models.ForeignKey('HedgeHog', on_delete=models.CASCADE)
#     comment = models.TextField()
#     visible = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)