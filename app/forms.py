from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length


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


class EditNoteForm(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()])
    body = TextAreaField(
        'Note: ',
        validators=[
            DataRequired(),
            Length(min=10, max=404)
        ]
    )
    submit = SubmitField('Edit')
