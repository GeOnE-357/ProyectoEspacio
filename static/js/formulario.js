var form = document.getElementsByTagName("form")[1],
elementos = form.elements,
total = elementos.length;

for (var i = 0; i < total; i++)
			{
				var nombre=elementos[i].name;
				nombre=nombre.charAt(0).toUpperCase()+nombre.slice(1)+"...";
				elementos[i].placeholder=nombre;
			}