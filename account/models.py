from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.CharField(max_length=100, blank=True)
    profile_picture_path = models.CharField(max_length=254, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    headline = models.CharField(max_length=200, blank=True)