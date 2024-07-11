from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/param/<arg>")
def hello_world2(arg):
    return f"<p>{arg}</p>"

@app.route("/sobre/<nome>/<idade>")
def sobre(nome, idade):
    return render_template('sobre.html', nome = nome, idade = idade)