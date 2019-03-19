from django.core.exceptions import ValidationError

def validate_dni(value):
    count = 0
    for c in str(value):
        count += 1
    if count <8:
            raise ValidationError("El numero es muy corto para ser un DNI.")
    return value

def validate_cel(value):
    count = 0
    for c in str(value):
        count += 1
    if count <8:
            raise ValidationError("El numero es muy corto para ser un celular.")
    return value

def validate_tel(value):
    count = 0
    for c in str(value):
        count += 1
    if count <6:
            raise ValidationError("El numero es muy corto para ser numero de telefono.")
    return value

def validate_str(value):
    string=value
    if string.isdigit():
        raise ValidationError("El campo ingresado no puede contener numeros.")
    return value

def validate_dir(value):
    a=value
    string=a.split()
    nom=False
    num=False
    for s in string:
        if s.isdigit():
            num=True
        else:
            nom=True
    if nom == False:
        raise ValidationError("La direccion no pueden ser solo numeros.")
    elif num == False:
        raise ValidationError("La direccion no tiene altura.")