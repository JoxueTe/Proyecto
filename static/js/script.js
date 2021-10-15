
function validar_formulario(){
    var username= document.getElementById("nombre");
    var contraseña= document.getElementById("pass");


    if (contraseña.value.length==0 || contraseña.value.length<4 ){
        alert("Ingrese una cotraseña con mas de 3 digitos");
        passid.focus();
        return false
    }

    if(username.value.length==0 || username.value.length<5){
        // Swal.fire(
        //   'heading',
        //   'text',
        //   'success'
        // )
        alert("El nombre debe ser mayor de 4 caracteres");
        console.log("Enviando formulario");
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

function send(){
    var id=document.getElementById("id");
    alert("entro")

    if (id.value.length==0 || id.value.length<3){
        alert("el codigo debe tener almenos 3 digitos");
        passid.focus();
        return false;
    }
}
