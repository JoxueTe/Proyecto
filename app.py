from flask import Flask, render_template
import forms, os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

dic_productos = [
    {'img': 'img/list.png', 'id': 1, 'name': 'Google Pixel 4', 'cantidad': '150', 'price': 500},
    {'img': 'img/list.png', 'id': 2, 'name': 'Google Pixel 4XL', 'cantidad': '40', 'price': 500},
    {'img': 'img/list.png', 'id': 3, 'name': 'Google Pixel 5', 'cantidad': '80', 'price': 500},
    {'img': 'img/list.png', 'id': 3, 'name': 'Google Pixel 5x', 'cantidad': '30', 'price': 500},
    {'img': 'img/list.png', 'id': 4, 'name': 'Google Pixel 5XL', 'cantidad': '180', 'price': 500}
]
 
dic_proveedores = [
    {'img': 'img/inventario.png', 'id': 1, 'name': 'Pepito Perez', 'telefono': '3201234589', 'price': 500},
    {'img': 'img/inventario.png', 'id': 2, 'name': 'Sutano Gonzalez', 'telefono': '3218564895', 'price': 500},
    {'img': 'img/inventario.png', 'id': 3, 'name': 'Mengano Beltrán', 'telefono': '3051257894', 'price': 500},
    {'img': 'img/inventario.png', 'id': 3, 'name': 'Juan ', 'telefono': '3125489654', 'price': 500},
    {'img': 'img/inventario.png', 'id': 4, 'name': 'Phone', 'telefono': '3215894123', 'price': 500}
]

dic_usuarios= [
    {'img': 'img/logo.png', 'id': 1, 'name': 'Pepito Perez', 'telefono': '3101527895', 'price': 500},
    {'img': 'img/logo.png', 'id': 2, 'name': 'Sutano Gonzalez', 'telefono': '3001234567', 'price': 500},
    {'img': 'img/logo.png', 'id': 3, 'name': 'Mengano Beltrán', 'telefono': '3051257894', 'price': 500},
    {'img': 'img/logo.png', 'id': 3, 'name': 'Juan ', 'telefono': '3208954123', 'price': 500},
    {'img': 'img/logo.png', 'id': 4, 'name': 'Phone', 'telefono': '3502157852', 'price': 500}
]
    
@app.route("/")
@app.route("/login")
def login_vista():
    return render_template('login.html')


@app.route("/recuperar")
def recuperar_vista():
    return render_template('recuperar.html')

@app.route("/productos")
def productos_vista():
    check = forms.FormCheckProduct()
    menu="Productos"
    return render_template('lista.html', menu=menu, items=dic_productos, check=check)

@app.route("/proveedores")
def proveedores_vista():
    menu="Proveedores"
    return render_template('lista.html', menu=menu, items=dic_proveedores)

@app.route("/usuarios")
def usuarios_vista():
    menu="Usuarios"
    return render_template('lista.html', menu=menu, items=dic_usuarios)

@app.route("/productos/registrar")
def registar_producto_vista():
    submenu="Registrar"
    menu="Productos"
    return render_template('formularioProducto.html', submenu=submenu, menu=menu, items=dic_productos)

@app.route("/productos/editar")
def editar_producto_vista():
    submenu="Editar"
    menu="Productos"
    return render_template('formularioProducto.html', submenu=submenu, menu=menu, items=dic_productos)

@app.route("/productos/informacion")
def info_producto_vista():
    submenu="Información"
    menu="Productos"
    return render_template('formularioProducto.html', submenu=submenu, menu=menu, items=dic_productos)

@app.route("/proveedores/registrar")
def registar_proveedor_vista():
    submenu="Registrar"
    menu="Proveedores"
    return render_template('formularioProUser.html', submenu=submenu, menu=menu, items=dic_proveedores)

@app.route("/proveedores/editar")
def editar_proveedor_vista():
    submenu="Editar"
    menu="Proveedores"
    return render_template('formularioProUser.html', submenu=submenu, menu=menu, items=dic_proveedores)

@app.route("/proveedores/informacion")
def info_proveedor_vista():
    submenu="Información"
    menu="Proveedores"
    return render_template('formularioProUser.html', submenu=submenu, menu=menu, items=dic_proveedores)

@app.route("/usuarios/registrar")
def registar_usuario_vista():
    submenu="Registrar"
    menu="Usuarios"
    check = forms.FormListUser()
    return render_template('formularioProUser.html', submenu=submenu, menu=menu, check=check, items=dic_usuarios)

@app.route("/usuarios/editar")
def editar_usuario_vista():
    submenu="Editar"
    menu="Usuarios"
    check = forms.FormListUser()
    return render_template('formularioProUser.html', submenu=submenu, menu=menu, check=check, items=dic_usuarios)

@app.route("/usuarios/informacion")
def info_usuario_vista():
    submenu="Información"
    menu="Usuarios"
    check = forms.FormListUser()
    return render_template('formularioProUser.html', submenu=submenu, menu=menu, check=check, items=dic_usuarios)