# Generated by Django 2.1.1 on 2018-11-24 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0001_initial'),
        ('personas', '0004_auto_20180926_1941'),
        ('cursos', '0003_auto_20180919_1451'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Asistencia',
            new_name='Inscripcion',
        ),
    ]
