from django.db import models

# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=40)
    contents = models.TextField()
    mainphoto = models.ImageField(blank=True,null=True)