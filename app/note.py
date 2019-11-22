from app import app
from app.forms import *
from app.models import *
from flask import flash
from flask import abort
from flask import url_for
from flask import request
from flask import redirect
from flask import render_template
from flask_login import login_required
from flask_login import current_user


def get_note(id):
    return Note.query.filter_by(id=id).first()


def get_tag(id):
    return Tag.query.filter_by(id=id).first()


def get_user(username):
    return User.query.filter_by(username=username).first()


def editors(row):
    names = [i.strip() for i in row.split(',')]
    users = [get_user(i) for i in names]
    return users[:6] if users[0] is not None else []


def get_editors_name(note):
    return ', '.join([i.username for i in note.users[1:]])

# def tag_dev(tags):
#     tags = tags.split(',')
#     for i in range(len(tags)):
#         tags[i] = tags[i].strip().replace(' ', '_')
#     return tags


@app.route('/create', methods=['POST', 'GET'])
@login_required
def create():
    form = CreateNoteForm()
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.all()]

    if form.validate_on_submit():
        print(editors(form.editors.data))
        note = Note(
            title=form.title.data,
            body=form.body.data,
            users=[current_user] + editors(form.editors.data),
            tags=[get_tag(id=form.tags.data)]
        )
        db.session.add(note)
        db.session.commit()
        flash('Created is successful!')
        return redirect(url_for('index'))
    return render_template('note/create.html', form=form)


@app.route('/note/<int:id>/edit', methods=['POST', 'GET'])
@login_required
def update(id):
    author = None

    note = get_note(id)
    form = CreateNoteForm()
    if note in current_user.notes:
        print(1)
        if request.method == 'GET':
            form.title.data = note.title
            form.body.data = note.body
            form.editors.data = get_editors_name(note)
            author = note.users[0]
        elif form.validate_on_submit():
            note.title = form.title.data
            note.body = form.body.data
            note.users = [current_user] + editors(form.editors.data),
            note.tags.choices = [(tag.id, tag.name) for tag in note.tags]
            db.session.commit()
            return redirect(url_for('index'))
    else:
        flash('You cant edit this note.')
        return redirect(url_for('index'))
    print(form.errors)
    return render_template('note/update.html', form=form, author=author)


@app.route('/note/<int:id>/delete', methods=['DELETE', 'GET'])
@login_required
def delete(id):
    note = get_note(id)
    if current_user == note.users[0]:
        note = get_note(id)
        db.session.delete(note)
        db.session.commit()
        flash('Note delete is successful.')
    else:
        abort(403)
    return redirect(url_for('index'))
