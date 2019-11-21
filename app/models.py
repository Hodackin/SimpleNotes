from app import db, login
from flask_login import UserMixin
from datetime import datetime


@login.user_loader
def load_user(id):
    return db.session.query(User).get(id)


user_notes = db.Table(
    'user_notes',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('note_id', db.Integer, db.ForeignKey('notes.id')),
)


note_tags = db.Table(
    'note_tags',
    db.Column('note_id', db.Integer, db.ForeignKey('notes.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<User id:{}, name:{}>'.format(self.id, self.username)


class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String(404), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(
        db.DateTime(),
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    users = db.relationship('User', secondary=user_notes, backref='notes')

    def __repr__(self):
        return '<Note id:{}, title:{}>'.format(self.id, self.title)


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    notes = db.relationship('Note', secondary=note_tags, backref='tags')

    def repr(self):
        return '<Tag id:{}, name:{}>'.format(self.id, self.name)
