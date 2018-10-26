from django.contrib import admin
from .models import Dependencia, Dia, Aula, Horario, DetalleAula

admin.site.register(Dependencia)
admin.site.register(Dia)
admin.site.register(Aula)
admin.site.register(Horario)
admin.site.register(DetalleAula)
