from django.db import models
from django.contrib.auth.models import User
from blog.models import Blog

# Create your models here.
class Comment(models.Model): 
	author = models.ForeignKey(User, on_delete=models.CASCADE) 
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments') 
	body = models.TextField() 
	approved = models.BooleanField(default=False) 
	created_on = models.DateTimeField(auto_now_add=True)