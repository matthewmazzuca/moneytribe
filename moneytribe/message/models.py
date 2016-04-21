from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

class Thread(models.Model):
	start_user = models.IntegerField(default = -1)
	start_user_fn = models.CharField(max_length=100, blank=True)
	second_user = models.IntegerField(default = -1)
	second_user_fn = models.CharField(max_length=100, blank=True)
	started_at = models.DateTimeField(auto_now_add=True, null=True)
	last_reply = models.DateTimeField(blank=True)
	last_message = models.TextField(blank=True)
	job = models.IntegerField(default = -1, blank = True)
	group = models.BooleanField(default=False)
	group_ids = models.TextField(blank=True)
	group_names = models.CharField(blank=True, max_length=100)

	def __str__(self):
		return self.start_user


class Message(models.Model):

	sender = models.IntegerField(default = -1)
	sender_fn = models.CharField(blank=True, max_length=100)
	recipient = models.IntegerField(default = -1)
	recipient_fn = models.CharField(blank=True, max_length=100)
	read = models.BooleanField(default = False)
	sent_at = models.DateTimeField(auto_now_add=True)
	read_at = models.DateTimeField(blank=True, null=True)
	replied_at = models.DateTimeField(blank=True, null=True)
	body = models.TextField()
	thread = models.ForeignKey(Thread, unique=False,on_delete=models.CASCADE)

	class Meta:
		ordering = ["sent_at"]
		# verbose_name_plural = "oxen"

	def __str__(self):
		return self.sender
