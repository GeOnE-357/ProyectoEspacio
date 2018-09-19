# Generated by Django 2.1.1 on 2018-09-19 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_auto_20180918_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='curso',
            name='mes',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='cursos.Mes'),
        ),
    ]
