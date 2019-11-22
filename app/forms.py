from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import SubmitField
from wtforms import SelectField
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from wtforms.validators import EqualTo
from wtforms.validators import Length


class CreateTagForm(FlaskForm):
    name = StringField('Tag: ', render_kw={'placeholder' : 'Your note body'})


class RegisterForm(FlaskForm):
    username = StringField(
        'Ussername: ',
        validators=[DataRequired()],
        render_kw={
            'placeholder' : 'Username'
            }
    )
    password = PasswordField(
        'Password: ',
        validators=[DataRequired()],
        render_kw={
            'placeholder' : 'Password'
        }
    )
    password2 = PasswordField(
        'Repeat Password: ',
        validators=[
            DataRequired(),
            EqualTo('password')
        ],
        render_kw={
            'placeholder' : 'Repeat password'
        }
    )
    submit = SubmitField('Sing up')


class LoginForm(FlaskForm):
    username = StringField(
        'Username: ',
        validators=[DataRequired()],
        render_kw={
            'placeholder' : 'Username'
            }
    )
    password = PasswordField(
        'Password: ',
        validators=[DataRequired()],
        render_kw={
            'placeholder' : 'Password'
        }
    )
    remember_me = BooleanField('Remember me: ')
    submit = SubmitField('Sing in')


class CreateNoteForm(FlaskForm):
    title = StringField(
        validators=[DataRequired()],
        render_kw={
            'placeholder' : 'Title'
        }
    )
    body = TextAreaField(
        validators=[
            DataRequired(),
            Length(min=10, max=404)
        ],
        render_kw={
            'placeholder' : 'Your note body'
        }
    )
    editors = StringField(render_kw={'placeholder' : 'Editors'})
    tags = SelectField(
        coerce=int,
        choices=[],
    )
    submit = SubmitField('Create')


