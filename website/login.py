from flask import Blueprint, render_template, request

login = Blueprint('login', __name__)


@login.route('/login.php', methods=['GET', 'POST'])
# Handler for GET, POST requests for '/login.php' endpoint.
def home():
    # If the request is GET we simply render the hebrew homepage to the student.
    if request.method == 'GET':
        return render_template('./login.html')

    # POST request is sent here only via redirection when user's credentials are wrong. (see courses_list.py line 20+)
    if request.method == 'POST':
        return render_template('./login_fail.html')
