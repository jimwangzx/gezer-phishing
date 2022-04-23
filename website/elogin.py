from flask import Blueprint, render_template, request

elogin = Blueprint('elogin', __name__)


@elogin.route('/elogin.php', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('./elogin.html')

    # POST request is sent here only via redirection when user's credentials are wrong.
    if request.method == 'POST':
        return render_template('./elogin_fail.html')
