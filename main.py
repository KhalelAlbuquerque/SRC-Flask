from flask import Flask, render_template, request, flash, redirect
import mysql.connector
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'palavra-secreta123'

@app.route('/')
def home():
    return render_template('html/login.html')

@app.route('/acesso')
def acesso():
    return render_template('html/acesso.html', userName=request.args.get('userName'))

@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    if request.method == "GET":
        return render_template('html/cadastro.html')

    elif request.method == "POST":
        user = request.form.get('user')
        password = request.form.get('password')

        comando = f'INSERT INTO usuario (user, password) VALUES ("{user}", "{password}")'

        cursor.execute(comando)
        conexao.commit()

        return redirect(f'/acesso?userName={user}')



@app.route('/login', methods=["POST"])
def login():
    usuario = request.form.get('user')
    senha = request.form.get('password')

    with open('usuarios.json') as f:
        lista = json.load(f)
        for c in lista:
            if c['nome'] == usuario and c['senha'] == senha:
                return redirect(f'/acesso?userName={c["nome"]}')

            flash('Login invalido')
            return redirect('/')





if __name__ in '__main__':
    conexao = mysql.connector.connect(host="localhost", user="root", password="1234", database="flask")
    cursor = conexao.cursor()




    app.run(debug=True)
    cursor.close()
    conexao.close()

