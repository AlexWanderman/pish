
# █░█ █ █▀▀ █░█░█ █▀   █▀█ █▀▀ █▀▀ █ █▀ ▀█▀ █▀▀ █▀█
# ▀▄▀ █ ██▄ ▀▄▀▄▀ ▄█   █▀▄ ██▄ █▄█ █ ▄█ ░█░ ██▄ █▀▄

from flask import render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import Email, InputRequired, Length

from app import db
from ...models.user import UserModel
from ..views import views


@views.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = UserModel()

        user.email = form.email.data
        user.username = form.username.data
        user.name = form.name.data
        user.password = form.password.data

        db.session.add(user)
        db.session.commit()

        return render_template('home.html')

    return render_template('profile/register.html', form=form)


class RegisterForm(FlaskForm):
    email = EmailField('Email', [InputRequired(),  Length(5, 80), Email()])
    username = StringField('Username', [InputRequired(), Length(2, 20)])
    name = StringField('Username', [InputRequired(), Length(2, 32)])
    password = PasswordField('Password', [InputRequired(), Length(8, 80)])
