
# █░█ █ █▀▀ █░█░█ █▀   █░░ █▀█ █▀▀ █ █▄░█
# ▀▄▀ █ ██▄ ▀▄▀▄▀ ▄█   █▄▄ █▄█ █▄█ █ █░▀█

from flask import render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import Email, InputRequired, Length

from ..views import views


@views.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return render_template('home.html')

    return render_template('profile/login.html', form=form)


class LoginForm(FlaskForm):
    email = EmailField('Email', [InputRequired(),  Length(5, 80), Email()])
    password = PasswordField('Password', [InputRequired(), Length(8, 80)])
