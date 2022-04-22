from flask import Blueprint, render_template, request, redirect, url_for
from libs.logic import Logic

crslist = Blueprint('courses_list', __name__)
logic = Logic()


@crslist.route('/crslist.php', methods=['POST'])
def crs_list():
    username, password, identity, is_heb = request.form.get('username'), request.form.get('pass'), request.form.get('id'), request.form.get('isheb')

    html_file_name = logic.render_courses(username, password, identity, is_heb)

    # Invalid credentials, redirect to login page.
    if html_file_name == '1':
        return redirect(url_for('login.home'), code=307)
    if html_file_name == '0':
        return redirect(url_for('elogin.home'), code=307)

    return render_template(f"./{html_file_name}")
