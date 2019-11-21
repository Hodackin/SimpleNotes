from app import app
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session
from flask import flash
from app.forms import *
from app.models import *
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask_login import login_required
from flask_login import current_user


def get_user(username):
    return User.query.filter_by(username=username).first()


@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data

        error = None
        user = get_user(username)
        if user is not None:
            error = 'Please use a different username.'
        else:
            user = User(
                username=username,
                password=generate_password_hash(
                    password=form.password2.data
                )
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))

        flash(error)
    return render_template('auth/register.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        error = None
        user = get_user(username)
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('index'))

        flash(error)
    return render_template('auth/login.html', title='Sing in', form=form)


@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash('Successfully logged out', 'success')
    return redirect(url_for('index'))
