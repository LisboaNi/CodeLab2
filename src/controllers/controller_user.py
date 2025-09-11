from config.database import db
from flask import render_template, request, redirect, url_for, flash

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