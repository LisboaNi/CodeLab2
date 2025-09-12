from config.database import db
from flask import render_template, request, redirect, url_for, flash, session

from models.model_music import Music, GenreEnum
from models.model_user import User

def list_music():
    if not session.get('username'):
        return redirect(url_for('main.authenticar'))
    
    user = User.query.filter_by(username=session.get('username')).first()
    musics = Music.query.order_by(Music.id).filter(user.id == Music.user_id).all()
    return render_template('views/list_music.html', list_music=musics)

def add_music():
    if not session.get('username'):
        return redirect(url_for('main.authenticar'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        artist = request.form.get('artist')
        genre = request.form.get('genre')

        user = User.query.filter_by(username=session.get('username')).first()
        music = Music.query.filter_by(name=name, user_id=user.id).first()

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
    
def edit_music(music_id):
    if not session.get('username'):
        return redirect(url_for('main.authenticar'))
    
    music = Music.query.get(music_id)

    if request.method == 'POST':
        music.name = request.form['name']
        music.artist = request.form['artist']
        music.genre = request.form['genre']

        db.session.commit()
        flash('Music updated successfully!', 'success')
        return redirect(url_for('main.list_music'))
    
    else:
        return render_template('views/edit_music.html', music=music, genres=GenreEnum)
    
def del_music(music_id):
    if not session.get('username'):
        return redirect(url_for('main.authenticar'))
    
    music = Music.query.get(music_id)
    db.session.delete(music)
    db.session.commit()
    flash('Music deleted successfully!', 'success')
    return redirect(url_for('main.list_music'))