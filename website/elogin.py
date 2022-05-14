from flask import Blueprint, render_template, request

# elogin as for English Login.
elogin = Blueprint('elogin', __name__)


@elogin.route('/elogin.php', methods=['GET', 'POST'])
# Handler for GET, POST requests for '/elogin.php' endpoint.
def home():

    # If the request is GET we simply render the english homepage to the student.
    if request.method == 'GET':
        return render_template('./elogin.html')

    # POST request is sent here only via redirection when user's credentials are wrong. (see courses_list.py line 20+)
    if request.method == 'POST':
        return render_template('./elogin_fail.html')
