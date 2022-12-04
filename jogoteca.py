from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#?


app.secret_key = 'qwertpoiuyt'

db = SQLAlchemy(app)

app.config['SQLALCHEMT_DATABASE_URL'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'ROOT',
        servidor = 'localhost',
        database = 'jogoteca'
    )


class Jogos(db.Model):
    id = db.Column(db.Interger, primary_key = True, autoincrement = True)
    nome = db.Column(db.String(50), nullable = False)
    categoria = db.Column(db.String(40), nullable = False)
    console = db.Column(db.String(20), nullable = False)
    def __repr__(self):
        return '<Name %r>' % self.name
class Usuario(db.Model):
    nickname = db.Column(db.String(20), primary_key = True)
    nome = db.Column(db.String(20), nullable = False)
    senha = db.Column(db.String(100), nullable = False)
    def __repr__(self):
        return '<Name %r>' % self.name
@app.route('/')
def index():
    lista = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo='Games', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='New Game')

@app.route('/criar', methods= ['POST'])
def criar():
    lista = Jogos.query.order_by(Jogos.id)
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogos(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = Usuario.query.filter_by(nickname = request.form['usuario']).first()
    if usuario:
        usuario = usuario[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo='Login', proxima = proxima)

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('logout efetuado')
    return redirect(url_for('index'))

app.run(debug=True)
