from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


def image_upload_to(instance, filename):
	return '%s/profile_img/%s' %(instance.user.id, filename)

class UserData(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True,
		default=1
		)
	first_name = models.CharField(blank=True, max_length=50)
	last_name = models.CharField(blank=True, max_length=50)
	first_time = models.BooleanField(default=True)
	income = models.CharField(blank=True, max_length=10)

	# image = models.ImageField(upload_to=image_upload_to, blank=True)
	# company info

	def __unicode__(self):
		return self.first_name

class UserAddress(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True,
		default=1
		)
	street = models.CharField(blank=True, max_length=50)
	city = models.CharField(blank=True, max_length=20)
	country = models.CharField(blank=True, max_length=20)
	postal = models.CharField(blank=True, max_length=20)


class UserDataImage(models.Model):

	user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
	image = models.ImageField(upload_to=image_upload_to, blank=True)
	title = models.CharField(max_length=100, blank=True)
	selected = models.BooleanField(default=False)
	extension = models.CharField(blank=True, max_length=10)

	def __unicode__(self):
		return self.title
