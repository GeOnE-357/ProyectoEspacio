var form = document.getElementsByTagName("form")[1];
form.addEventListener('submit', function(event)
	{
		event.preventDefault()
		var a = true,
		elementos = this.elements,
		total = elementos.length;

		for (var i = 0; i < total; i++)
			{
			if (!elementos[i].value.length)
				{
  					elementos[i].focus();
  					a = false;
  					break;
  				}
			}
		if (a)
			{
			window.scrollTo(0,0);
			document.getElementsByClassName("contenedor")[0].style.display="block";		
			this.submit();
			}
	},false)