# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-07 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoresLibro', '0002_auto_20180606_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoreslibro',
            name='capituloSel',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
