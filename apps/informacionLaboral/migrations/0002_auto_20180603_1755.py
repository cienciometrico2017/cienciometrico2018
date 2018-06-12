# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-03 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('informacionLaboral', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacionlaboral',
            name='carrera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carrera.carrera'),
        ),
        migrations.AlterField(
            model_name='informacionlaboral',
            name='facultad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facultad.facultad'),
        ),
        migrations.AlterField(
            model_name='informacionlaboral',
            name='tipoContrato',
            field=models.CharField(blank=True, choices=[('Servicios Ocasionales', 'Servicios Ocasionales'), ('Nombramiento Titular Auxiliar 1', 'Nombramiento Titular Auxiliar 1'), ('Nombramiento Titular Auxiliar 2', 'Nombramiento Titular Auxiliar 2'), ('Nombramiento Titular Agregado 1', 'Nombramiento Titular Agregado 1'), ('Nombramiento Titular Agregado 2', 'Nombramiento Titular Agregado 2'), ('Nombramiento Principal 1', 'Nombramiento Principal 1'), ('Nombramiento Principal 2', 'Nombramiento Principal 2')], max_length=200, null=True),
        ),
    ]