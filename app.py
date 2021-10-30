from flask import Flask, render_template, request, redirect, url_for,flash
from database.database_controller import *
from flask.helpers import url_for
from werkzeug.security import check_password_hash, generate_password_hash
import forms, os
from flask_login import LoginManager
import smtplib



app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
# SECRET_KEY = 'misiontic'

#--------------------------------< RUTA PRINCIPAL DE LOGUEO >-----------------------------
@app.route("/")
@app.route("/login")
def login_vista():
    return render_template('login.html')

@app.route("/logueo", methods=['POST'])
def logueo():
    username=request.form['nombre']
    password_usuario=request.form['pass']
    print("nombre de usuario "+ username)
    print("Contraseña ingresada "+ password_usuario)
    consulta_usua= consult_name(username)
    consulta_email=consult_email(username)

    # result=check_password_hash()
    if consulta_usua :
        print("prueba por usuario")
        consulta_pass=consult_password(username)
        contra=consulta_pass[0]
        if check_password_hash(contra,password_usuario):
            print("Cotraseña correcta")
            nombre_usua=consult_nombre_usua(username)
            name_usuario=nombre_usua[0]
            success_message = 'Bienvenido {}'.format(name_usuario)
            flash(success_message)
            return render_template('dashboard.html')
        else:
            print("contraseña incorrecta")
            success_mensage='Usuario o contraseña incorrecta, favor verificar'
            flash(success_mensage)
            return render_template('login.html')
    elif consulta_email :
        print("prueba por email")
        consulta_password_email=consult_password_email(username)
        contraseña=consulta_password_email[0]
        if check_password_hash(contraseña,password_usuario):
            print("contraseña correcta por email")
            nombre_usua=consult_nombre_email(username)
            name_usuario=nombre_usua[0]
            success_message = 'Bienvenido {}'.format(name_usuario)
            flash(success_message)
            return render_template('dashboard.html',)
        else:
            success_mensage='Usuario o contraseña incorrecta, favor verificar'
            flash(success_mensage)
            return render_template('login.html')
    else:
        app.logger.info('El usuario no existe')
        success_mensage='Usuario o contraseña incorrecta, favor verificar'
        flash(success_mensage)
        return render_template('login.html')

#---------------------------------< RUTA DE RECUPERAR CONTRASEÑA >----------------------------
@app.route("/recuperar")
def recuperar_vista():
    return render_template('recuperar.html')

@app.route("/recuperar/enviado", methods=['POST'])
def recuperar():
    email=request.form['email']
    consulta_email=consult_email(email)
    if consulta_email:
        print("Correo encontrado")
    else:
        success_mensage='Correo no registrado, favor verificar'
        flash(success_mensage)
        return render_template('recuperar.html')
    return render_template('recuperar.html')

#-------------------------------< VISTA DEL DASHBOARD >--------------------------------------
@app.route("/dashboard")
def dashboard_vista():
    return render_template('dashboard.html')

#-----------------------------------< RUTAS DE PRODUCTOS >----------------------------------------------
@app.route("/productos")
def productos_vista():
    check = forms.FormCheckProduct()
    productos=get_all_producto()
    menu="Productos"
    return render_template('lista.html', menu=menu, check=check, tablas=productos)

@app.route("/productos/registrar")
def registrar_producto_vista():
    submenu="Registrar"
    menu="Productos"
    return render_template('formularioProducto.html', submenu=submenu, menu=menu)

@app.route("/productos/editar/<int:id>")
def editar_producto_vista(id):
    producto=get_one_producto(id)
    submenu="Editar"
    menu="Productos"
    return render_template('formularioProducto.html', submenu=submenu, menu=menu, tabla=producto)

@app.route("/productos/informacion/<int:id>")
def info_producto_vista(id):
    producto=get_one_producto(id)
    submenu="Información"
    menu="Productos"
    return render_template('formularioProducto.html', submenu=submenu, menu=menu, tabla=producto)

@app.route('/create-Productos', methods=['POST'])
def create_productos():
    id=request.form['id']
    nombre=request.form['nombre']
    cantidadminima=request.form['cantidadminima']
    cantidadmaxima=request.form['cantidadmaxima']
    cantidadexistencia=request.form['cantidadexistencia']
    precio=request.form['precio']
    cantidadprov=request.form['cantidadprov']
    fregistro=request.form['fregistro']
    descripcion=request.form['descripcion']
    img=request.form['img']
    proveedores=request.form['prov']
    insert_producto(id,nombre,cantidadminima,cantidadmaxima,descripcion,img,fregistro,cantidadexistencia,proveedores,precio,cantidadprov)
    return redirect(url_for('registrar_producto_vista'))

@app.route('/update-Productos', methods=['POST'])
def update_productos():
    id=request.form['id']
    nombre=request.form['nombre']
    cantidadminima=request.form['cantidadminima']
    cantidadmaxima=request.form['cantidadmaxima']
    cantidadexistencia=request.form['cantidadexistencia']
    precio=request.form['precio']
    cantidadprov=request.form['cantidadprov']
    fregistro=request.form['fregistro']
    descripcion=request.form['descripcion']
    img=request.form['img']
    proveedores=request.form['prov']
    if img=='':
        dataimg=get_one_producto(id)
        img=dataimg[5]
    edit_producto(id,nombre,cantidadminima,cantidadmaxima,descripcion,img,fregistro,cantidadexistencia,proveedores,precio,cantidadprov)
    return redirect(url_for('editar_producto_vista',id=id))

@app.route('/delete-Productos/<id>', methods=['GET'])
def delete_producto(id):
    dell_producto(id) 
    return redirect(url_for('productos_vista'))

#----------------------------------Proveedor--------------------------------------------
@app.route("/proveedores")
def proveedores_vista():
    proveedores=get_all_proveedor()
    menu="Proveedores"
    return render_template('lista.html', menu=menu, tablas=proveedores)

@app.route("/proveedores/registrar")    
def registrar_proveedor_vista():
    submenu="Registrar"
    menu="Proveedores"
    return render_template('formularioProUser.html', submenu=submenu, menu=menu)

@app.route("/proveedores/editar/<int:id>")
def editar_proveedor_vista(id):
    proveedor=get_one_proveedor(id)
    submenu="Editar"
    menu="Proveedores"
    return render_template('formularioProUser.html', submenu=submenu, menu=menu, tabla=proveedor)

@app.route("/proveedores/informacion/<int:id>", methods=["GET"])
def info_proveedor_vista(id):
    proveedor=get_one_proveedor(id)
    submenu="Información"
    menu="Proveedores"
    return render_template('formularioProUser.html', submenu=submenu, menu=menu, tabla=proveedor)

@app.route('/create-Proveedores', methods=['POST'])
def create_proveedor():
    id=request.form['id']
    nombre=request.form['nombre']
    direccion=request.form['direccion']
    email=request.form['email']
    img=request.form['img']
    fregistro=request.form['fregistro']
    ciudad=request.form['ciudad']
    telefono=request.form['telefono']
    descripcion=request.form['descripcion']
    if img=='':
        img='proveedores-icon.png'
    insert_proveedor(id,nombre,direccion,email,fregistro,img,ciudad,telefono,descripcion)
    return redirect(url_for('registrar_proveedor_vista'))


@app.route('/update-Proveedores', methods=['POST'])
def update_proveedor():
    id=request.form['id']
    nombre=request.form['nombre']
    direccion=request.form['direccion']
    email=request.form['email']
    img=request.form['img']
    fregistro=request.form['fregistro']
    ciudad=request.form['ciudad']
    telefono=request.form['telefono']
    descripcion=request.form['descripcion']
    if img=='':
        dataimg=get_one_proveedor(id)
        img=dataimg[5]
    edit_proveedor(id,nombre,direccion,email,fregistro,img,ciudad,telefono,descripcion)
    return redirect(url_for('editar_proveedor_vista',id=id))

@app.route('/delete-Proveedores/<id>', methods=['GET'])
def delete_proveedor(id):
    dell_proveedor(id)      
    return redirect(url_for('proveedores_vista'))


#---------------------------------------Usuario--------------------------------------------
@app.route("/usuarios")
def usuarios_vista():
    usuarios=get_all_usuario()
    menu="Usuarios"
    return render_template('lista.html', menu=menu, tablas=usuarios)

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
    return render_template('formularioProUser.html', submenu=submenu, menu=menu, tabla=usuario)

@app.route("/usuarios/informacion/<int:id>", methods=["GET"])
def info_usuario_vista(id):
    usuario=get_one_usuario(id)
    submenu="Información"
    menu="Usuarios"
    return render_template('formularioProUser.html', submenu=submenu, menu=menu, tabla=usuario)

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
    password=password
    password=generate_password_hash(password)
    if img=='':
        img='usuarios-icon.png'
    insert_usuario(id,nombre,usuario,password,email,img,fregistro,rol,telefono)
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
    comp=get_one_usuario(id)
    comparacion=comp[3]
    print(img)
    if comparacion == password :
        print("Son iguales")
        password=password
    else:
        print("Son diferentes")
        password=password
        password=generate_password_hash(password)
    if img=='':
        dataimg=get_one_usuario(id)
        img=dataimg[5]
    edit_usuario(id,nombre,usuario,password,email,img,fregistro,rol,telefono)
    return redirect(url_for('editar_usuario_vista',id=id))

@app.route('/delete-Usuarios/<id>', methods=['GET'])
def delete_usuario(id):
    dell_usuario(id)      
    return redirect(url_for('usuarios_vista'))

#---------------------------< ACTUAIZACION DE CAMBIOS >--------------------------------------
if __name__ == '__main__':
    app.run(debug=True)

# Función para enviar correo desde Python con librería smtplib
def enviarCorreo(asunto, mensaje, destinatarios):
    cuerpo = 'Subject: {}\n\n{}'.format(asunto, mensaje)

    servidor = smtplib.SMTP('smtp-mail.outlook.com', 25)
    servidor.starttls()

    servidor.login('jelds.mintic.2022@hotmail.com', 'Kt$zk48pVEZ?=')

    servidor.sendmail('jelds.mintic.2022@hotmail.com', destinatarios, cuerpo)
    servidor.quit()

    print('Correo enviado exitosamente')
