from flask import Flask, render_template

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
