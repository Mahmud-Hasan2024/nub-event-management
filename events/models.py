from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    category = models.ForeignKey("Category", related_name='events', on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='events')
    image = CloudinaryField('image', default='default_images/q3xcrnqej6ticrb5kuvq', blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
