var time = 5;
function contador()
	{
	if(time > 0) {
      document.getElementById("contador").innerHTML = "Seras redireccionado en <b>"+ time + "</b> segundos.";
      time--;
    } 
    else {
     	 location.href="/" //Redirecciona al index.
    	}
    }

setInterval(contador, 1000)