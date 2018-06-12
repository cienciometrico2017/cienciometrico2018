# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-04 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0002_remove_proyecto_integrantes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='estado',
            field=models.CharField(blank=True, choices=[('En espera de Presupuesto', 'En espera de Presupuesto'), ('En Ejecución', 'En Ejecución'), ('Finalizado', 'Finalizado')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='financiamiento',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='lineaInvestigacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Linea_Investigacion.linea_investigacion'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='montoFinanciado',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='montorecibido',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='resumen',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='subLinea',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sub_Lin_Investigacion.sub_lin_investigacion'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='tipoProyecto',
            field=models.CharField(blank=True, choices=[('Formativo', 'Formativo'), ('Generativo', 'Generativo')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='titulo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]