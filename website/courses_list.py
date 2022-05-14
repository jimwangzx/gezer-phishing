from flask import Blueprint, request, redirect, url_for
from libs.logic import Logic

crslist = Blueprint('courses_list', __name__)
logic = Logic()


@crslist.route('/crslist.php', methods=['POST'])
# Handler for POST requests in '/crslist.php' endpoint.
def crs_list():

    # Retrieving the request's payload
    username, password, identity, is_heb = request.form.get('username'), request.form.get('pass'), request.form.get('id'), request.form.get('isheb')

    # Getting student's grades authentic HTML page. (See /libs/logic.py for 'business logic')
    html_file = logic.render_courses(username, password, identity, is_heb)

    # Invalid credentials, redirect to login page.
    #   If html_file == '1' we redirect the student to the Hebrew homepage while preserving request's properties.
    #   If html_file == '0' we redirect the student to the English homepage while preserving request's properties.
    if html_file == '1':
        return redirect(url_for('login.home'), code=307)
    if html_file == '0':
        return redirect(url_for('elogin.home'), code=307)

    return html_file
