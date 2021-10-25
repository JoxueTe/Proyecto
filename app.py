from flask import Flask, render_template, request, redirect, url_for
from database.database_controller import *
from database.db import get_db
from flask.helpers import url_for
from werkzeug.security import check_password_hash, generate_password_hash
import forms, os



app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
# SECRET_KEY = 'misiontic'


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
    check = forms.FormCheckProduct()
    menu="Productos"
    return render_template('lista.html', menu=menu, check=check)

@app.route("/proveedores")
def proveedores_vista():
    menu="Proveedores"
    return render_template('lista.html', menu=menu)

@app.route("/usuarios")
def usuarios_vista():
    usuarios=get_all_usuario()
    print(usuarios)
    menu="Usuarios"
    return render_template('lista.html', menu=menu, usuarios=usuarios)

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
    return render_template('formularioProUser.html', submenu=submenu, menu=menu)

@app.route("/usuarios/editar/<int:id>", methods=["GET"])
def editar_usuario_vista(id):
    usuario=get_one_usuario(id)
    submenu="Editar"
    menu="Usuarios"
    return render_template('formularioProUser.html', submenu=submenu, menu=menu, usuario=usuario)

@app.route("/usuarios/informacion/<int:id>", methods=["GET"])
def info_usuario_vista(id):
    usuario=get_one_usuario(id)
    check = forms.FormCheckProduct()
    submenu="Información"
    menu="Usuarios"
<<<<<<< HEAD
    return render_template('formularioProUser.html', submenu=submenu, menu=menu, check=check, usuario=usuario)
=======
    check = forms.FormListUser()
    return render_template('formularioProUser.html', submenu=submenu, menu=menu, check=check)
>>>>>>> 62179fceb7f4eca16c5853568287406c02cb418b

@app.route('/create-Usuarios', methods=['POST'])
def create_usuario():
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
    # insert_usuario(id,nombre,usuario,password,email,img,fregistro,rol,telefono)
    db.execute("INSERT INTO usuario (identif_usua,nom_usua, usuari_usua, passw_usua, email_usua, img_usua, fecha_ingreso_usua, rol_usua, tel_usua) "+
                "VALUES(?,?,?,?,?,?,?,?,?)",(id,nombre,usuario,password,email,img,fregistro,rol,telefono))
    db.commit()
    db.close()
    return redirect(url_for('registrar_usuario_vista'))

@app.route('/update-Usuarios', methods=['POST'])
def update_usuario():
    id=request.form['content']
    nombre=request.form['nombre']
    usuario=request.form['usuario']
    email=request.form['email']
    password=request.form['password']
    telefono=request.form['telefono']
    fregistro=request.form['fregistro']
    rol=request.form['rol']
    img=request.form['img']
    password=password+usuario
    password=generate_password_hash(password)
    edit_usuario(id,nombre,usuario,password,email,img,fregistro,rol,telefono)
    return redirect(url_for('editar_usuario_vista',id=id))

@app.route('/delete-Usuarios/<id>', methods=['GET'])
def delete_usuario(id):
    dell_usuario(id)      
    return redirect(url_for('usuarios_vista'))



if __name__ == '__main__':
    app.run(debug=True)

