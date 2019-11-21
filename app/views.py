from app import app
from flask import render_template, redirect, url_for, request, session, make_response, flash
from app.forms import *
from app.models import *
from flask_login import login_required, current_user


@app.route('/')
def index():
    tags = Tag.query.all()
    notes = Note.query.order_by(Note.updated_on)[::-1]
    return render_template('home.html', title='Home', notes=notes, tags=tags)


@app.route('/user/note')
@login_required
def user_notes():
    notes = current_user.notes
    return render_template('home.html', title='Home', notes=notes)


@app.route('/notes/tag/<int:id>')
def get_note_by_tag(id):
    tags = Tag.query.all()
    tag = Tag.query.filter_by(id=id).first()
    # notes = Note.query.filter(Note.tags.id == id).all()
    return render_template('home.html', title='Home', notes=tag.notes, tags=tags)

