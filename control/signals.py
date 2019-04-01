from django.db.models.signals import post_save
from datetime import datetime, date, time, timedelta
from django.dispatch import receiver
from django.contrib.auth.models import User
from asistencia.models import Asistencia
from cursos.models import Curso, Materia, Inscripcion
from dependencia.models import Dependencia, Aula, DetalleAula, Dia, Horario
from personas.models import Profesor, Alumno, Estudio
from .models import Log

@receiver(post_save, sender=User)
def create_user(sender, instance, raw, created, **kwargs):
	if created:
		u=User.objects.order_by('-last_login').first() #Usuario que lo creo.
		dni=str(u.username) 
		nombre= str(u.first_name+" "+u.last_name)
		tabla=str(instance._meta.db_table)#Nombre de la tabla.
		objeto=int(instance.id)
		fecha=datetime.today()
		accion="CREAR"	
		Log.objects.create(dni=dni,nombre=nombre,accion=accion,tabla=tabla,objeto=objeto,fecha=fecha)

@receiver(post_save, sender=Asistencia)
@receiver(post_save, sender=Curso)
@receiver(post_save, sender=Materia)
@receiver(post_save, sender=Inscripcion)
@receiver(post_save, sender=Dependencia)
@receiver(post_save, sender=Aula)
@receiver(post_save, sender=DetalleAula)
@receiver(post_save, sender=Dia)
@receiver(post_save, sender=Horario)
@receiver(post_save, sender=Asistencia)
@receiver(post_save, sender=Profesor)
@receiver(post_save, sender=Alumno)
@receiver(post_save, sender=Estudio)
def create_persona(sender, instance, raw, created, **kwargs):
	u=User.objects.order_by('-last_login').first() #Usuario que lo creo.
	dni=str(u.username) 
	nombre= str(u.first_name+" "+u.last_name)
	tabla=str(instance._meta.db_table)#Nombre de la tabla.
	objeto=int(instance.id)
	fecha=datetime.today()
	if created:
		accion="CREAR"	
	else:
		accion="ACTUALIZAR"
	Log.objects.create(dni=dni,nombre=nombre,accion=accion,tabla=tabla,objeto=objeto,fecha=fecha)