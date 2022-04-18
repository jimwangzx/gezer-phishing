from flask import Flask
from .login import login

app = Flask(__name__)
app.register_blueprint(login, url_prefix='/')