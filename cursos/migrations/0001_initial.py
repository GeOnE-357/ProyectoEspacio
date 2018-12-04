# Generated by Django 2.1.1 on 2018-12-03 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modulo', models.IntegerField(blank=True)),
                ('fInicio', models.DateField()),
                ('fFin', models.DateField()),
                ('anio', models.IntegerField(blank=True)),
                ('estado', models.CharField(max_length=15)),
                ('cantClases', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('alumnoID', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='personas.Alumno')),
                ('cursoID', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='cursos.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='materiaID',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='cursos.Materia'),
        ),
        migrations.AddField(
            model_name='curso',
            name='profesorID',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='personas.Profesor'),
        ),
    ]
