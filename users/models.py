from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_image = CloudinaryField('image', default='default_images/vt7vpmt0jpiapfyws2bh', blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username