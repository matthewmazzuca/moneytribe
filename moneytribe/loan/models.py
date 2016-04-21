from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from lender.models import Lender


class Loan(models.Model):
	user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
	name = models.CharField(blank=True, max_length=20)
	purchased = models.BooleanField(default=False)
	is_users = models.BooleanField(default=False)
	rate = models.CharField(blank=True, max_length=20)
	amount= models.CharField(blank=True, max_length=20)
	amount_left= models.CharField(blank=True, max_length=20)
	date = models.DateTimeField(auto_now_add=True)
	lender = models.ForeignKey(Lender, unique=False)
	broker = models.CharField(blank=True, max_length=20)

	def __str__(self):
		return self.name

class LoanDetail(models.Model):
	user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
	name= models.CharField(blank=True, max_length=20)
	objective= models.CharField(blank=True, max_length=20)
	consolidate = models.CharField(blank=True, max_length=20)
	has_property = models.BooleanField(default=False)
	when_to_buy = models.DateTimeField(blank=True)
	amount = models.CharField(blank=True, max_length=20)
	current_loan = models.BooleanField(default=True)
	loan_remaining = models.CharField(blank=True, max_length=20)
	rate = models.CharField(blank=True, max_length=20)
	other = models.TextField(blank=True)

	def __str__(self):
		return self.name

class LoanShare(models.Model):
	first_user = models.CharField(blank=True, max_length=20)
	second_user = models.CharField(blank=True, max_length=20)
	name = models.CharField(blank=True, max_length=20)
	loan = models.CharField(blank=True, max_length=20)
	broker = models.CharField(blank=True, max_length=20)
	advisor = models.CharField(blank=True, max_length=20)

	def __str__(self):
		return self.name