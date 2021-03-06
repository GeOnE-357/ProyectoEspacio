# Generated by Django 2.1.1 on 2019-06-19 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField(blank=True)),
                ('whatsapp', models.BigIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleAula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=20)),
                ('mes', models.CharField(max_length=10)),
                ('anio', models.IntegerField(blank=True)),
                ('aulaId', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='dependencia.Aula')),
                ('cursoID', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='cursos.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='detalleaula',
            name='diaId',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='dependencia.Dia'),
        ),
        migrations.AddField(
            model_name='detalleaula',
            name='horaId',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='dependencia.Horario'),
        ),
        migrations.AddField(
            model_name='aula',
            name='dependenciaId',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='dependencia.Dependencia'),
        ),
    ]
