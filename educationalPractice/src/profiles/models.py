from django.contrib.auth.models import AbstractUser
from django.db import models


class userNet(AbstractUser):
    """Custom user model"""
    middleName = models.CharField(max_length=50)
    firstLogin = models.DateTimeField(null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)


