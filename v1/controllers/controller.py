from flask import render_template, request, redirect, session, flash, url_for
from models.model import Musica, Usuario

lista = []

user01 = Usuario('admin', 'admin', 'admin')

users = {
    user01.login: user01
}

def listar():

    if not session.get('usuario'):
        return redirect(url_for('logar'))
    
    return render_template('lista.html', titulo = 'Minha lista', lista=lista)

def cadastrar():

    if not session.get('usuario'):
        return redirect(url_for('logar'))
    
    return render_template('cadastro.html', titulo = 'Cadastrar Musica')

def adicionar():
    nome = request.form['nome']
    cantor = request.form['cantor']
    genero = request.form['genero']

    add = Musica(nome, cantor, genero)

    lista.append(add)

    return redirect(url_for('index'))

def logar():
    return render_template('login.html', titulo = 'Login')


def autenticar():
    if request.form['usuario'] in users:

        user = users[request.form['usuario']]

        if user.senha == request.form['senha']:
            session['usuario'] = request.form['usuario']
            flash(f'Login do {user.usuario} realizado com sucesso!')
            return redirect(url_for('index'))
    
        else:
            flash('Usuário ou senha inválidos!')
            return redirect(url_for('logar'))

def logout():
    session.pop('usuario', None)
    return redirect(url_for('logar'))