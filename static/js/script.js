
function validar_formulario(){
    var username= document.getElementById("nombre");
    var contraseña= document.getElementById("pass");

    if(username.value.length==0 || username.value.length<3){
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

    if (contraseña.value.length==0 || contraseña.value.length<8 ){
        alert("Ingrese una cotraseña");
        passid.focus();
        return false;
    }

}

function Validar_contraseña(){
    var contraseña=document.getElementById('contra')
    if (contraseña.value.length==0 || contraseña.value.length<8 ){
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

function send(){
    var id=document.getElementById("id");
    alert("entro")

    if (id.value.length==0 || id.value.length<3){
        alert("el codigo debe tener almenos 3 digitos");
        passid.focus();
        return false;
    }
}

function previsualizar(){
    document.getElementById("seleccionArchivos").onchange = function(e) {
        // Creamos el objeto de la clase FileReader
        let reader = new FileReader();
      
        // Leemos el archivo subido y se lo pasamos a nuestro fileReader
        reader.readAsDataURL(e.target.files[0]);
      
        // Le decimos que cuando este listo ejecute el código interno
        reader.onload = function(){
          let preview = document.getElementById('preview'),
                  image = document.createElement('img');
      
          image.src = reader.result;
      
          preview.innerHTML = '';
          preview.append(image);
        };
    }
}


document.getElementById("vision").onmouseover = function() {mouseOver()};
document.getElementById("vision").onmouseout = function() {mouseOver()};

function mouseOver() {
    document.getElementById("vision");
        let input_contrasena = document.getElementById('password')
        let tipo_input = input_contrasena.getAttribute('type')
        if (tipo_input == 'password') {
            input_contrasena.setAttribute('type', 'text')
            document.getElementById("vision").setAttribute('src', '/static/img/hidden.png')
        } else {
            input_contrasena.setAttribute('type', 'password')
            document.getElementById("vision").setAttribute('src', '/static/img/view.png')
        }
}