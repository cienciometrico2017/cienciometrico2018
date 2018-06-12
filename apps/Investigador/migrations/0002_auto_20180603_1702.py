# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-03 22:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('roles', '0001_initial'),
        ('Investigador', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='investigador',
            name='roles',
            field=models.ManyToManyField(blank=True, to='roles.Rol'),
        ),
        migrations.AddField(
            model_name='investigador',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
