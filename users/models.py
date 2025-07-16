from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_image = models.ImageField(
        upload_to='profile_images/', blank=True, default='profile_images/default.png'
    )
    phone_number = models.CharField(max_length=14, blank=True)

    def __str__(self):
        return self.username