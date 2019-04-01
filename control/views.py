from django.shortcuts import render
from django.contrib.auth.models import Group
from .models import Log

def controlLog(request):
	if request.user in Group.objects.get(name="Gerente").user_set.all() or request.user.is_superuser:
		incidentes = Log.objects.all().order_by("-fecha")
		return render(request, 'control/index.html', {'lista':incidentes})
	else:
		tipo='neg'
		tit='ACCESO DENEGADO'
		men='No tiene los permisos necesarios para realizar esta tarea.'
		return render(request, 'mensaje.html', {'tipo':tipo, 'titulo':tit, 'mensaje':men})