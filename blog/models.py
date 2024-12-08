from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from profiles.models import TypeOfFish, TypeOfFishing

# Create your models here.

STATUS_CHOICES = (
        (0, 'Draft'),
        (1, 'Published')
    )

class Blog(models.Model):

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    favourite_fish = models.ForeignKey(TypeOfFish, on_delete=models.SET_NULL, null=True, blank=True)
    favourite_fishing = models.ForeignKey(TypeOfFishing, on_delete=models.SET_NULL, null=True, blank=True)

 
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} was written by {self.author}"

# Override the save method to auto-generate a slug if it's empty
    def save(self, *args, **kwargs):
        if not self.slug:  # Only set the slug if it's empty
            self.slug = slugify(self.title)  # Create the slug from the title
        super().save(*args, **kwargs)  # Call the parent class's save method

