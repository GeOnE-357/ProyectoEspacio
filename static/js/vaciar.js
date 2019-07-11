var vaciar = document.getElementById("vaciar");
vaciar.addEventListener('click', function(event)
	{
		window.scrollTo(0,0);
		document.getElementsByClassName("contenedor")[0].style.display="block";
	},false);