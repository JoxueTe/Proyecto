from flask import Flask, render_template
# import math

app = Flask(__name__)

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


@app.route("/usuarios")
def usuarios_vista():
    var="Usuarios"
    return render_template('lista.html', menu=var, items=dic_usuarios)

@app.route("/productos")
def productos_vista():
    var="Productos"
    return render_template('lista.html', menu=var, items=dic_productos)

@app.route("/proveedores")
def proveedores_vista():
    var="Proveedores"
    return render_template('lista.html', menu=var, items=dic_proveedores)

@app.route("/registrarproducto")
def registar_producto_vista():
    var="Registrar"
    return render_template('formularioProducto.html', submenu=var, items=dic_proveedores)

@app.route("/editarproducto")
def editar_producto_vista():
    var="Editar"
    return render_template('formularioProducto.html', submenu=var, items=dic_proveedores)

@app.route("/infoproducto")
def info_producto_vista():
    var="Información"
    return render_template('formularioProducto.html', submenu=var, items=dic_proveedores)