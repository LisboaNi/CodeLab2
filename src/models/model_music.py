import enum

from config.database import db
from sqlalchemy import Enum

class GenreEnum(enum.Enum):
    Pop = "Pop"
    Rock = "Rock"
    Jazz = "Jazz"
    Funk = "Funk"
    Eletronica = "Eletronica"

class Music(db.Model):

    __tablename__ = 'musics'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    artist = db.Column(db.String(120), nullable=False)
    genre = db.Column(Enum(GenreEnum), nullable=False)
    cover = db.Column(db.LargeBinary, nullable=True) 

    def __repr__(self):
        return f'<Music {self.name} by {self.artist}>'