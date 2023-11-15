from flask import Flask, render_template, request, flash, redirect
import mysql.connector
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'palavra-secreta123'

@app.route('/acesso')
def acesso():
    if request.args.get('userName')==None:
        flash('Rota protegida, faça o login pra continuar')
        return redirect('/login')
 
    return render_template('html/acesso.html', userName=request.args.get('userName'))

@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    if request.method == "GET":
        return render_template('html/cadastro.html')

    elif request.method == "POST":
        user = request.form.get('user')
        password = request.form.get('password')

        comando = f'SELECT * FROM usuario WHERE user="{user}"'
        cursor.execute(comando)
        result = cursor.fetchall()

        if result:
            flash('Usuário já cadastrado, escolha outro nome')
            return redirect('/cadastro')
        else:
            hashedPass = bcrypt.generate_password_hash(password).decode('utf-8')
            comando = f'INSERT INTO usuario (user, password) VALUES ("{user}", "{hashedPass}")'

            cursor.execute(comando)
            conexao.commit()

            return redirect(f'/acesso?userName={user}')

        



@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('html/login.html')
    elif request.method == "POST":
        usuario = request.form.get('user')
        senha = request.form.get('password')

        comando = f'SELECT * FROM usuario WHERE user="{usuario}"'
        cursor.execute(comando)
        result = cursor.fetchall()

        if result:
            dbUser = result[0][1]
            dbPass = result[0][2]
            print(senha, dbPass)
            if bcrypt.check_password_hash(dbPass, senha):
                return redirect(f'/acesso?userName={dbUser}')
            else:
                flash('Usuário não encontrado. Verifique suas credenciais.')
                return redirect('/login')
        else:
            flash('Usuário não encontrado. Verifique suas credenciais.')
            return redirect('/login')





if __name__ in '__main__':
    conexao = mysql.connector.connect(host="localhost", user="root", password="1234", database="flask")
    cursor = conexao.cursor()

    app.run(debug=True)
    
    cursor.close()
    conexao.close()

