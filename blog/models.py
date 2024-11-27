from django.db import models


from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

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

    def __str__(self):
        return self.title