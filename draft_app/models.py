from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="category_images")

    def __str__(self):
    	return self.name

class Termin(models.Model):
    title = models.SlugField(max_length=255)
    abbreviation = models.SlugField(max_length=50)
    longed = models.CharField(max_length=255)
    category = models.ManyToManyField(to=Category)
    image = models.ImageField(upload_to="draft_images")
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()

    def __str__(self):
    	return self.title

