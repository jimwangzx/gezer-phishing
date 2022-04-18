from flask import Blueprint, render_template, request, redirect
from libs.logic import Logic


login = Blueprint('login', __name__)
logic = Logic()


@login.route('/login', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('./index.html')

    if request.method == 'POST':
        username, password, identity = request.form.get('username'), request.form.get('pass'), request.form.get('id')

        logic.save(username, password, identity)
        html_file_name = logic.render_courses(username, password, identity)

        return render_template(f"./{html_file_name}")
