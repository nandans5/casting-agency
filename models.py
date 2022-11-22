# check movie and actor relationship
import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
# from settings import DB_NAME, DB_USER, DB_PASSWORD
from flask_migrate import Migrate

database_name = 'tests'
database_path = "postgresql://{}:{}@{}/{}".format('postgres', '28251532', 'localhost:5433', database_name)

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

    # migrate = Migrate(app, db)

class Movie(db.Model):

    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_month = Column(String)
    # actors = relationship('Actor', backref="movie", lazy=True)
    # actors = db.relationship('Actor', backref='movie') # check

    def __init__(self, title, release_month):
        self.title = title
        self.release_month = release_month

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_month': self.release_month,
            # 'movies': list(map(lambda actor: movie.format(), self.movies))
        }

'''
Actor
'''


class Actor(db.Model):

    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    # movie_id = Column(Integer, ForeignKey('movies.id'), nullable=True)
    # movie_id = db.Column(db.Integer, db.ForeignKey('Movie.id'))

    def __init__(self, name, age, gender, movie_id):
        self.name = name
        self.age = age
        self.gender = gender
        self.movie_id = movie_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            # "movie_id": self.movie_id
        }