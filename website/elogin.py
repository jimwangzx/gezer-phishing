from flask import Blueprint, render_template, request, redirect, url_for
from libs.logic import Logic


elogin = Blueprint('elogin', __name__)
logic = Logic()


@elogin.route('/elogin.php', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('./elogin.html')

    if request.method == 'POST':
        username, password, identity = request.form.get('username'), request.form.get('pass'), request.form.get('id')

        html_file_name = logic.render_courses(username, password, identity, english=True)
        if html_file_name == "elogin_fail.html":
            return render_template(f"./{html_file_name}")

        return redirect(url_for('courses_list.crs_list', username=html_file_name))
