from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo ('Forza', 'Corrida', 'Multiplataforma')
jogo2 = Jogo ('Counter-Strike: Global Offensive', 'Tiro', 'PC')
jogo3 = Jogo ('The Last of Us', 'ação-aventura', 'PlayStation')
lista = [jogo1, jogo2, jogo3]


class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha


usuario1 = Usuario("pedro amorim", "bigp", "098iop")
usuario2 = Usuario("lyank silva", "lyank", "lyly")
usuario3 = Usuario("arthur", "dan", "morreumamando")

usuarios = { usuario1.nickname : usuario1,
             usuario2.nickname : usuario2,
             usuario3.nickname : usuario3}

app.secret_key = 'qwertpoiuyt'


@app.route('/')
def index():
    return render_template('lista.html', titulo='Games', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='New Game')

@app.route('/criar', methods= ['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
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
