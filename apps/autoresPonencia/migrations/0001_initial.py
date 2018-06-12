# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-04 05:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ponencia', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='autoresPonencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradoAutoria', models.CharField(max_length=150)),
                ('ponencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Ponencia.ponencia')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('ver_autores', 'ver autores'),),
            },
        ),
    ]
