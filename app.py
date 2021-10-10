from flask import Flask, render_template
import math

app = Flask(__name__)

@app.route("/")
@app.route("/login")
def login_vista():
    return render_template('login.html')


@app.route("/recuperar")
def recuperar_vista():
    return render_template('recuperar.html')


@app.route("/home")
def home_vista():
    return render_template('base.html')

@app.route("/usuarios")
def usuarios_vista():
    items = [
    {'img': 'img\inventario.png', 'id': 1, 'name': 'Pepito Perez', 'cantMin': '893212299897', 'price': 500},
    {'img': 'img\inventario.png', 'id': 2, 'name': 'Sutano Gonzalez', 'cantMin': '893212299897', 'price': 500},
    {'img': 'img\inventario.png', 'id': 3, 'name': 'Mengano Beltrán', 'cantMin': '893212299897', 'price': 500},
    {'img': 'img\inventario.png', 'id': 3, 'name': 'Juan ', 'cantMin': '893212299897', 'price': 500},
    {'img': 'img\inventario.png', 'id': 4, 'name': 'Phone', 'cantMin': '893212299897', 'price': 500}
]
    size=math.ceil(len(items)/4)
    var="Usuarios"
    return render_template('lista.html', menu=var, items=items, size=size)

@app.route("/productos")
def productos_vista():
    items = [
    {'img': 'img\inventario.png', 'id': 1, 'name': 'Google Pixel 4', 'cantMin': '893212299897', 'price': 500},
    {'img': 'img\inventario.png', 'id': 2, 'name': 'Google Pixel 4XL', 'cantMin': '893212299897', 'price': 500},
    {'img': 'img\inventario.png', 'id': 3, 'name': 'Google Pixel 5', 'cantMin': '893212299897', 'price': 500},
    {'img': 'img\inventario.png', 'id': 3, 'name': 'Google Pixel 5x', 'cantMin': '893212299897', 'price': 500},
    {'img': 'img\inventario.png', 'id': 4, 'name': 'Google Pixel 5XL', 'cantMin': '893212299897', 'price': 500}
]
    size=math.ceil(len(items)/4)
    var="Productos"
    return render_template('lista.html', menu=var, items=items, size=size)

@app.route("/proveedores")
def proveedores_vista():
    items = [
    {'img': 'img\inventario.png', 'id': 1, 'name': 'Pepito Perez', 'cantMin': '893212299897', 'price': 500},
    {'img': 'img\inventario.png', 'id': 2, 'name': 'Sutano Gonzalez', 'cantMin': '893212299897', 'price': 500},
    {'img': 'img\inventario.png', 'id': 3, 'name': 'Mengano Beltrán', 'cantMin': '893212299897', 'price': 500},
    {'img': 'img\inventario.png', 'id': 3, 'name': 'Juan ', 'cantMin': '893212299897', 'price': 500},
    {'img': 'img\inventario.png', 'id': 4, 'name': 'Phone', 'cantMin': '893212299897', 'price': 500}
]
    size=math.ceil(len(items)/4)
    var="Proveedores"
    return render_template('lista.html', menu=var, items=items, size=size)