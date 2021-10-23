from flask import Flask, render_template, request, redirect, url_for
from flask.helpers import url_for
from database.db import get_db 
from werkzeug.security import check_password_hash, generate_password_hash

 
app = Flask(__name__)
SECRET_KEY = 'misiontic'
    
@app.route("/")
@app.route("/login")
def login_vista():
    return render_template('login.html')


@app.route("/recuperar")
def recuperar_vista():
    return render_template('recuperar.html')

@app.route("/dashboard")
def dashboard_vista():
    return render_template('dashboard.html')

@app.route("/productos")
def productos_vista():
    menu="Productos"
    return render_template('lista.html', menu=menu)

@app.route("/proveedores")
def proveedores_vista():
    menu="Proveedores"
    return render_template('lista.html', menu=menu)

@app.route("/usuarios")
def usuarios_vista():
    menu="Usuarios"
    return render_template('lista.html', menu=menu)

@app.route("/productos/registrar")
def registrar_producto_vista():
    submenu="Registrar"
    menu="Productos"
    return render_template('formularioProducto.html', submenu=submenu, menu=menu)

@app.route("/productos/editar")
def editar_producto_vista():
    submenu="Editar"
    menu="Productos"
    return render_template('formularioProducto.html', submenu=submenu, menu=menu)

@app.route("/productos/informacion")
def info_producto_vista():
    submenu="Información"
    menu="Productos"
    return render_template('formularioProducto.html', submenu=submenu, menu=menu)

@app.route("/proveedores/registrar")
def registrar_proveedor_vista():
    submenu="Registrar"
    menu="Proveedores"
    return render_template('formularioProUser.html', submenu=submenu, menu=menu)

@app.route("/proveedores/editar")
def editar_proveedor_vista():
    submenu="Editar"
    menu="Proveedores"
    return render_template('formularioProUser.html', submenu=submenu, menu=menu)

@app.route("/proveedores/informacion")
def info_proveedor_vista():
    submenu="Información"
    menu="Proveedores"
    return render_template('formularioProUser.html', submenu=submenu, menu=menu)

@app.route("/usuarios/registrar")
def registrar_usuario_vista():
    submenu="Registrar"
    menu="Usuarios"
    # check = forms.FormListUser()
    return render_template('formularioProUser.html', submenu=submenu, menu=menu)

@app.route('/create-Usuarios', methods=['POST'])
def create():
    id=request.form['content']
    nombre=request.form['nombre']
    usuario=request.form['usuario']
    email=request.form['email']
    password=request.form['password']
    telefono=request.form['telefono']
    fregistro=request.form['fregistro']
    rol=request.form['rol']
    img=request.form['img']
    print('aqui se imprime la variabe'+img)
    db=get_db()
    password=password+usuario
    password=generate_password_hash(password)
    db.execute("INSERT INTO usuarios (identificacion,img, nombre, usuario, password , email, telefono, fregistro, rol ) "+
                "VALUES(?,?,?,?,?,?,?,?,?)",(id,img,nombre,usuario,password,email,telefono,fregistro,rol))
    db.commit()  
    db.close()          
    return redirect(url_for('registrar_usuario_vista'))


@app.route("/usuarios/editar")
def editar_usuario_vista():
    submenu="Editar"
    menu="Usuarios"
    # check = forms.FormListUser()
    return render_template('formularioProUser.html', submenu=submenu, menu=menu)

@app.route("/usuarios/informacion")
def info_usuario_vista():
    submenu="Información"
    menu="Usuarios"
    # check = forms.FormListUser()
    return render_template('formularioProUser.html', submenu=submenu, menu=menu)

if __name__ == '__main__':
    app.run(debug=True)