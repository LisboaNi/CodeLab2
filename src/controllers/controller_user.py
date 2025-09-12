from config.database import db
from flask import render_template, request, redirect, url_for, flash, session

from models.model_user import User

def add_user():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
    
        user = User.query.filter_by(username=username).first()

        if user:
            flash('User already registered!', 'error')
            return redirect(url_for('main.add_user'))
        
        else:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            flash('User added successfully!', 'success')
            return redirect(url_for('main.list_music'))
    else:
        return render_template('views/add_user.html')
    
def authenticar():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session['username'] = request.form['username']
            flash(f'Login {user.username} successful!', 'success')
            return redirect(url_for('main.list_music'))
        else:
            flash('Invalid username or password!', 'error')
            return redirect(url_for('main.authenticar'))
    else:
        return render_template('views/login.html')

def logout():
    session.pop('username', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('main.authenticar'))