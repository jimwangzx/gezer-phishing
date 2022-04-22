from flask import Blueprint, render_template, request

login = Blueprint('login', __name__)


@login.route('/login.php', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('./login.html')
    if request.method == 'POST':
        return render_template('./login_fail.html')
