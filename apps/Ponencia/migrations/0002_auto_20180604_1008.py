# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-04 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ponencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ponencia',
            name='financia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='universidad.universidad'),
        ),
    ]
