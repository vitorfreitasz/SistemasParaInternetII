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
    teste = ['FLASKASSO']*8
    return render_template('sobre.html', nome, idade, teste)

@app.route('/variaveis')
def usando_variaveis():
    chamada = {12: 'Joao', 13:'Pablo', 14: 'Filipa'}
    return render_template('chamada.html', chamada=chamada)