from django.contrib import admin
from .models import Dependencia, Aula, Dia, Horario 

admin.site.register(Dependencia)
admin.site.register(Aula)
admin.site.register(Dia)
admin.site.register(Horario)