# Generated by Django 2.0.7 on 2018-09-14 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
        ('dependencia', '0003_auto_20180913_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleaula',
            name='cursoID',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='cursos.Curso'),
        ),
    ]
