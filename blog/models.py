from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date_created = models.DateTimeField(auto_now_add=True)


	class Meta:
		ordering = ('-date_created',)
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'

	def __str__(self):
		return self.title