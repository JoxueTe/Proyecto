
function validar_formulario(){
    var username= document.getElementById("nombre");
    var contraseña= document.getElementById("pass");

    if(username.value.length==0 || username.value.length<8){
        // Swal.fire(
        //   'heading',
        //   'text',
        //   'success'
        // )
        alert("Ingrese un nombre correctamente");
        console.log("Enviando formulario")
        passid.focus();
        return false;
    }

    if (contraseña.value.length==0 || contraseña.value.length<3 ){
        alert("Ingrese una cotraseña");
        passid.focus();
        return false;
    }

}

function validar_correo(){
    var email=document.getElementById("correo")

    if (email.value.length==0 || !/\S+@\S+\.\S+/i.test(email.value)){
        alert("Ingrese correo");
        console.log("enviando")
        return false;
    }
}


// function eliminar(){
//     prompt("Eliminar")
// }


var btnAbrirPopup = document.getElementById('btn-eliminar'),
	overlay = document.getElementById('overlay'),
	popup = document.getElementById('popup'),
	btnCerrarPopup = document.getElementById('btn-cerrar-popup');

btnAbrirPopup.addEventListener('click', function(){
	overlay.classList.add('active');
	popup.classList.add('active');
});

btnCerrarPopup.addEventListener('click', function(e){
	e.preventDefault();
	overlay.classList.remove('active');
	popup.classList.remove('active');
});




// <div id="borrar">
//                             <!-- <form action="">
//                                 <input type="button" id="btn_eliminar" value="" onclick="eliminar()">
//                             </form>
//                             <script src="/static/js/script.js"></script> -->
//                             <button type="image" src={{ url_for('static', filename='img/delete.png') }} class="sobre" id="btn-abrir-popup"></button>
//                             <div class="overlay" id="overlay">
//                                 <div class="popup" id="popup">
//                                     <a href="#" id="btn-cerrar-popup" class="btn-cerrar-popup"><i class="fas fa-times"></i></a>
//                                     <h3>SUSCRIBETE</h3>
//                                     <h4>y recibe un cupon de descuento.</h4>
//                                     <form action="">
//                                         <div class="contenedor-inputs">
//                                             <input type="text" placeholder="Nombre">
//                                             <input type="email" placeholder="Correo">
//                                         </div>
//                                         <input type="submit" class="btn-submit" value="Suscribirse">
//                                     </form>
//                                 </div>
//                             </div>
//                         </div>
//                         <script src="/static/js/script.js"></script>