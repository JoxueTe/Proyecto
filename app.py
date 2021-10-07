from flask import Flask, render_template

app = Flask(__name__)

@app.route("/login")
def login_vista():
    return render_template('login.html')


@app.route("/recuperar")
def recuperar_vista():
    return render_template('recuperar.html')
