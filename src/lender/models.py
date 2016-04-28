from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Lender(models.Model):
	user = models.ForeignKey(User, blank=True, unique=False)
	company = models.CharField(blank=True, max_length=20)

	def __str__(self):
		return self.company



class Product(models.Model):
	lender = models.ForeignKey(Lender, unique=False, on_delete=models.CASCADE)
	name = models.CharField(blank=True, max_length=20)
	rank = models.CharField(blank=True, max_length=20)
	rate = models.CharField(blank=True, max_length=20)

	def __str__(self):
		return self.name
