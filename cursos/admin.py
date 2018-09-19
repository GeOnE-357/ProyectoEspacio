from django.contrib import admin
from .models import Curso, Materia, Asistencia, Mes
# Register your models here.
admin.site.register(Curso)
admin.site.register(Materia)
admin.site.register(Asistencia)
admin.site.register(Mes)