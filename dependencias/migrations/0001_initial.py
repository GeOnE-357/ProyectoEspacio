# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-06 01:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=15)),
                ('telefono', models.IntegerField(blank=True)),
                ('whatsapp', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=10)),
                ('aulaId', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='dependencias.Aula')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.IntegerField(blank=True)),
                ('estado', models.CharField(max_length=10)),
                ('diaId', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='dependencias.Dia')),
            ],
        ),
        migrations.AddField(
            model_name='aula',
            name='dependenciaId',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='dependencias.Dependencia'),
        ),
    ]
