from flask import Flask
from .login import login
from .elogin import elogin
from .courses_list import crslist

app = Flask(__name__)
app.register_blueprint(login, url_prefix='/meser')
app.register_blueprint(elogin, url_prefix='/meser')
app.register_blueprint(crslist, url_prefix='/meser')
