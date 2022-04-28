from flask import Blueprint, request, redirect, url_for
from libs.logic import Logic

crslist = Blueprint('courses_list', __name__)
logic = Logic()


@crslist.route('/crslist.php', methods=['POST'])
def crs_list():
    username, password, identity, is_heb = request.form.get('username'), request.form.get('pass'), request.form.get('id'), request.form.get('isheb')

    html_file = logic.render_courses(username, password, identity, is_heb)

    # Invalid credentials, redirect to login page.
    if html_file == '1':
        return redirect(url_for('login.home'), code=307)
    if html_file == '0':
        return redirect(url_for('elogin.home'), code=307)

    return html_file
