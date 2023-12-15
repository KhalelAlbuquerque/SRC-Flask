from flask import Flask, render_template, request, flash, redirect, abort, session
import mysql.connector
from flask_bcrypt import Bcrypt
from flask_session import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'palavra-secreta123'
app.config['SESSION_TYPE'] = 'filesystem'

bcrypt = Bcrypt(app)
Session(app)

@app.route('/acesso')
def acesso():
    if 'username' not in session:
        flash('Rota protegida, faça o login pra continuar')
        return redirect('/login')
 
    return render_template('html/acesso.html', userName=session["username"])

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

            session['username'] = user
            return redirect(f'/acesso?userName={session["username"]}')

        
@app.route('/info')
def info():
    id = request.args.get('id')
    print(request.args)

    try:
        # Reabrir a conexão e criar um novo cursor
        connection = mysql.connector.connect(user='root', password='1234', host='localhost', database='flask')
        cursor = connection.cursor()

        comando = f'SELECT * FROM usuario WHERE idUsuario="{id}"'
        cursor.execute(comando)

        result = cursor.fetchall()
        print(result)
        
    except mysql.connector.Error as e:
        print(f"Erro na consulta SQL: {e}")

    finally:
        # Fechar o cursor e a conexão, mesmo em caso de exceção
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection is not None:
            connection.close()

    return render_template('html/info.html', userName=id)




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

        # sql injection
        # senha = '" OR "1"="1"; -- '

        if result:
            dbUser = result[0][1]
            dbPass = result[0][2]
            if bcrypt.check_password_hash(dbPass, senha):
                session['username'] = usuario
                print(session)
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

    app.run(debug=True, port=3000, host='0.0.0.0')
    
    cursor.close()
    conexao.close()

