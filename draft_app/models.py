from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.SlugField(max_length=15)
    image = models.ImageField(upload_to="category_images")

    def __str__(self):
    	return self.name

class Termin(models.Model):
    title = models.CharField(max_length=255)
    abbreviation = models.SlugField(max_length=50)
    longed = models.CharField(max_length=255)
    category = models.ManyToManyField(to=Category)
    image = models.ImageField(upload_to="draft_images", null=True, blank=True)
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    text = RichTextField(null=True, blank=True)

    def __str__(self):
    	return self.title

class Post(models.Model):
	title = models.CharField(max_length=255)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	posttype = models.CharField(max_length=20, choices=( ('post', 'post'), ('tool', 'tool') ), default='post')

	def __str__(self):
		return self.title

class Block(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class ImageBlock(Block):
	image = models.ImageField(upload_to="image_block_images")
	title = models.CharField(max_length=255)

	def __str__(self):
		return self.title

class TextBlock(Block):
	header = models.CharField(max_length=255)
	text = models.TextField()

	def __str__(self):
		return self.title

class CodeBlock(Block):
	body = models.TextField()
