from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

def image_upload_to(instance, filename):
	return '%s/%s' %(instance.user.id, filename)

class File(models.Model):

	user = models.ForeignKey(User, unique=False)
	title = models.CharField(max_length=100, blank=True)
	file = models.FileField(upload_to=image_upload_to, blank=True)
	extension = models.CharField(blank=True, max_length=10)
	is_image = models.BooleanField(default=False)
	is_doc = models.BooleanField(default=False)
	is_pdf = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.title
