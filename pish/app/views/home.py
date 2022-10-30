
# █░█ █ █▀▀ █░█░█ █▀   █░█ █▀█ █▀▄▀█ █▀▀
# ▀▄▀ █ ██▄ ▀▄▀▄▀ ▄█   █▀█ █▄█ █░▀░█ ██▄

from flask import render_template
from .views import views


@views.route('/', methods=['GET'])
def home():
    return render_template('home.html')
