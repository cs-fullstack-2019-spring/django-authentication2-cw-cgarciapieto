from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogModel(models.Model):
    username= models.CharField(max_length=100)
    blog_title= models.CharField(max_length=100)
    blog_entry=models.TextField(max_length=500)
    blog_user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)


