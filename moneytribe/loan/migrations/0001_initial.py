# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 05:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lender', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('purchased', models.BooleanField(default=False)),
                ('is_users', models.BooleanField(default=False)),
                ('rate', models.CharField(blank=True, max_length=20)),
                ('amount', models.CharField(blank=True, max_length=20)),
                ('amount_left', models.CharField(blank=True, max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('broker', models.CharField(blank=True, max_length=20)),
                ('lender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lender.Lender')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LoanDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('objective', models.CharField(blank=True, max_length=20)),
                ('consolidate', models.CharField(blank=True, max_length=20)),
                ('has_property', models.BooleanField(default=False)),
                ('when_to_buy', models.DateTimeField(blank=True)),
                ('amount', models.CharField(blank=True, max_length=20)),
                ('current_loan', models.BooleanField(default=True)),
                ('loan_remaining', models.CharField(blank=True, max_length=20)),
                ('rate', models.CharField(blank=True, max_length=20)),
                ('other', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LoanShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_user', models.CharField(blank=True, max_length=20)),
                ('second_user', models.CharField(blank=True, max_length=20)),
                ('name', models.CharField(blank=True, max_length=20)),
                ('loan', models.CharField(blank=True, max_length=20)),
                ('broker', models.CharField(blank=True, max_length=20)),
                ('advisor', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
