# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-03 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datos_profecionales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Profecion', models.CharField(max_length=255)),
                ('Grado_Cientifico', models.CharField(max_length=255)),
                ('Categoria', models.CharField(max_length=255)),
            ],
            options={
                'permissions': (('ver_datosprofesionales', 'ver datosprofesionales'),),
            },
        ),
    ]
