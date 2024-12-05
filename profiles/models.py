from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

class TypeOfFish(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TypeOfFishing(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)  # Allow blank initially
    profile_pic = CloudinaryField('image', default='placeholder', transformation={
        'width': 350,
        'height': 350,
        'crop': 'fill',
        'gravity': 'face',
        'quality': 'auto:good',
        'fetch_format': 'auto'
    })
    favourite_fish = models.ForeignKey(TypeOfFish, on_delete=models.SET_NULL, null=True)
    favourite_fishing = models.ForeignKey(TypeOfFishing, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Only set slug if it's not already set
            self.slug = slugify(self.user.username)  # Generate slug from username
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s Profile"

