from config.database import db
from flask import render_template, request, redirect, url_for, flash

from models.model_music import Music, GenreEnum
from models.model_user import User

def list_music():
    musics = Music.query.order_by(Music.id).all()
    return render_template('views/list_music.html', list_music=musics)

def add_music():
    if request.method == 'POST':
        name = request.form.get('name')
        artist = request.form.get('artist')
        genre = request.form.get('genre')

        music = Music.query.filter_by(name=name).first()
        user = User.query.first()

        if music:
            flash('Music already registered!', 'error')
            return redirect(url_for('main.add_music'))
        else:
            music = Music(user_id=user.id, name=name, artist=artist, genre=genre)
            db.session.add(music)
            db.session.commit()
            flash('Music added successfully!', 'success')
            return redirect(url_for('main.list_music'))
        
    else:
        return render_template('views/add_music.html', genres=GenreEnum)